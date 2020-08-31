""" Periodic table's views
"""

from typing import Dict, Any, List
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

import core_main_app.components.version_manager.api as version_manager_api
import core_main_app.utils.decorators as decorators
from core_explore_common_app.components.query import api as query_api
from core_explore_common_app.utils.query.query import create_default_query
from core_explore_common_app.views.user.views import (
    ResultsView,
    ResultQueryRedirectView,
)
from core_explore_keyword_app.views.user.views import KeywordSearchView
from core_main_app.commons.exceptions import DoesNotExist
from core_main_app.settings import DATA_SORTING_FIELDS
from core_explore_periodic_table_app.views.user.form import PeriodicTableForm
from core_main_app.utils.rendering import render
from core_main_app.components.template import api as template_api
import core_explore_periodic_table_app.permissions.rights as rights
from core_explore_periodic_table_app.components.search_operator_mapping import (
    api as search_operator_mapping_api,
)
from core_explore_keyword_app.components.search_operator import (
    api as search_operator_api,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table import (
    api as persistent_query_periodic_table_api,
)


class PeriodicTableBuildQueryView(KeywordSearchView):
    results_url = "core_explore_periodic_table_results"
    query_builder_interface = (
        "core_explore_periodic_table_app/user/periodic_table/periodic.html"
    )

    @method_decorator(
        decorators.permission_required(
            content_type=rights.explore_periodic_table_content_type,
            permission=rights.explore_periodic_table_access,
            login_url=reverse_lazy("core_main_app_login"),
        )
    )
    def get(self, request, **kwargs):
        """GET

        Args:
            request:
            **kwargs:

        Returns:

        """
        query_id = str(kwargs["query_id"]) if "query_id" in kwargs else None

        # assets / modals / forms
        context = self._get(request, query_id)

        return render(
            request,
            "core_explore_periodic_table_app/user/index.html",
            assets=self.assets,
            modals=self.modals,
            context=context,
        )

    def _get(self, request, query_id):
        """Prepare the GET context

        Args:
            query_id:

        Returns:

        """
        error = None
        # set the correct default ordering for the context
        default_order = ",".join(DATA_SORTING_FIELDS)
        if query_id is None:
            # create query
            query = create_default_query(request, [])
            # upsert the query
            query_api.upsert(query)
            # create all data for select values in forms
            periodic_table_data_form = {
                "query_id": str(query.id),
                "user_id": query.user_id,
            }
        else:  # query_id is not None
            try:
                # get the query id
                query = query_api.get_by_id(query_id)
                user_id = query.user_id

                # get all elements back
                elements = self._parse_query(query.content)

                # get all version managers
                version_managers = []
                for template in query.templates:
                    version_managers.append(
                        str(version_manager_api.get_from_version(template).id)
                    )
                # create all data for select values in forms
                periodic_table_data_form = {
                    "query_id": str(query.id),
                    "user_id": user_id,
                    "elements": elements,
                    "global_templates": version_managers,
                    "order_by_field": super().build_sorting_context_array(query),
                    "user_templates": version_managers,
                }
                # set the correct ordering for the context
                if periodic_table_data_form["order_by_field"] != 0:
                    default_order = periodic_table_data_form["order_by_field"]
            except Exception as e:
                error = (
                    "An unexpected error occurred while loading the query: {}.".format(
                        str(e)
                    )
                )
                return {"error": error}

        search_form = PeriodicTableForm(data=periodic_table_data_form)
        return self._format_keyword_search_context(
            search_form, error, None, default_order
        )

    @method_decorator(
        decorators.permission_required(
            content_type=rights.explore_periodic_table_content_type,
            permission=rights.explore_periodic_table_access,
            login_url=reverse_lazy("core_main_app_login"),
        )
    )
    def post(self, request):
        """POST

        Args:
            request:

        Returns:

        """

        # assets / modals / forms
        context = self._post(request)

        return render(
            request,
            "core_explore_periodic_table_app/user/index.html",
            assets=self.assets,
            modals=self.modals,
            context=context,
        )

    def _post(self, request):
        """Prepare the POST context

        Args:
            request:

        Returns:

        """
        error = None
        warning = None
        search_form = PeriodicTableForm(data=request.POST)
        # validate form
        if search_form.is_valid():
            try:
                # get form values
                query_id = search_form.cleaned_data.get("query_id", None)
                elements = search_form.cleaned_data.get("elements", None)
                global_templates = search_form.cleaned_data.get("global_templates", [])
                user_templates = search_form.cleaned_data.get("user_templates", [])
                order_by_field_array = (
                    search_form.cleaned_data.get("order_by_field", "")
                    .strip()
                    .split(";")
                )
                # get all template version manager ids
                template_version_manager_ids = global_templates + user_templates
                # from ids, get all version manager
                version_manager_list = version_manager_api.get_by_id_list(
                    template_version_manager_ids
                )
                # from all version manager, build a list of all version (template)
                template_ids = []
                list([template_ids.extend(x.versions) for x in version_manager_list])
                if query_id is None or elements is None:
                    error = "Expected parameters are not provided"
                else:
                    # get query
                    query = query_api.get_by_id(query_id)
                    if len(query.data_sources) == 0:
                        warning = "Please select at least 1 data source."
                    else:
                        # update query
                        query.templates = template_api.get_all_by_id_list(template_ids)

                        element_search_operators = (
                            self._format_keyword_to_search_operators(
                                elements.split(",")
                            )
                        )

                        if not element_search_operators:
                            warning = "No search operators has been configured, please contact an administrator."
                            element_search_operators = ""

                        query.content = self._build_query(element_search_operators)
                        # set the data-sources filter value according to the POST request field
                        for data_sources_index in range(len(query.data_sources)):
                            # update the data-source filter only if it's not a new data-source
                            # (the default filter value is already added when the data-source
                            # is created)
                            if data_sources_index in range(
                                0, len(order_by_field_array)
                            ):
                                query.data_sources[
                                    data_sources_index
                                ].order_by_field = order_by_field_array[
                                    data_sources_index
                                ]

                        query_api.upsert(query)
            except DoesNotExist as does_not_exist_error:
                error = (
                    str(does_not_exist_error)
                    if does_not_exist_error
                    else "An unexpected error occurred while retrieving the query."
                )
            except Exception as e:
                error = "An unexpected error occurred: {}.".format(str(e))
        else:
            error = "An unexpected error occurred: the form is not valid."

        return self._format_keyword_search_context(
            search_form,
            error,
            warning,
            search_form.cleaned_data.get("order_by_field", "").strip(),
        )

    def _load_assets(self):
        """Return assets structure

        Returns:

        """

        assets = ResultsView._load_assets(self)
        extra_assets: Dict[str, List[Any]] = {
            "js": [
                {
                    "path": "core_explore_periodic_table_app/user/js/periodic_table/periodic.js",
                    "is_raw": False,
                },
                {
                    "path": "core_explore_periodic_table_app/user/js/persistent_query.raw.js",
                    "is_raw": True,
                },
            ],
            "css": [
                "core_explore_keyword_app/user/css/search/search.css",
                "core_explore_periodic_table_app/user/css/periodic_table/periodic.css",
            ],
        }

        assets["js"].extend(extra_assets["js"])
        assets["css"].extend(extra_assets["css"])

        return assets

    def _format_keyword_search_context(
        self, search_form, error, warning, query_order=""
    ):
        """Format the context for the periodic table research page

        Args:
            search_form:
            error:
            warning:
            query_order:

        Returns:

        """
        context = super()._format_keyword_search_context(
            search_form, error, warning, query_order=query_order
        )
        context["results_url"] = "core_explore_periodic_table_results"

        return context

    def _format_keyword_to_search_operators(self, elements_list):
        """Format the elements list to a set of search operators

        Args:
            elements_list: (ex. ["Au","U"...])

        Returns: search operator list (ex.["so1:Au", "so2:Au", "so1:U", "so2:U"]) | None
        """
        result = []
        all_so_mapping = search_operator_mapping_api.get_all()

        if all_so_mapping.count() > 0:
            for so_mapping in all_so_mapping:
                so = search_operator_api.get_by_id(str(so_mapping.search_operator.id))
                for element in elements_list:
                    result.append(f"{so.name}:{element}")
        else:
            result = None

        return result

    @staticmethod
    def get_description():
        """Get the description page

        Returns:

        """
        return (
            "Click on an element of the Periodic Table to add it to your query. "
            "You can save queries and you will retrieve them on your next connection. "
            "When your query is done, please click on Submit Query to get XML documents that match the criteria."
        )

    @staticmethod
    def get_title():
        """Get the title page

        Returns:

        """
        return "Periodic Table"


class ResultQueryRedirectPeriodicSearchView(ResultQueryRedirectView):
    @staticmethod
    def _get_persistent_query(persistent_query_id):
        return persistent_query_periodic_table_api.get_by_id(persistent_query_id)

    @staticmethod
    def _get_reversed_url(query):
        return reverse(
            "core_explore_periodic_table_index", kwargs={"query_id": query.id}
        )

    @staticmethod
    def _get_reversed_url_if_failed():
        return reverse("core_explore_periodic_table_index")
