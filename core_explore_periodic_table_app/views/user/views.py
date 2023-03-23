""" Periodic table's views
"""

from typing import Dict, Any, List

from django.urls import reverse
from django.utils.decorators import method_decorator

import core_main_app.components.template_version_manager.api as template_version_manager_api
import core_main_app.utils.decorators as decorators
from core_explore_common_app.components.query import api as query_api
from core_explore_common_app.views.user.views import (
    ResultsView,
    ResultQueryRedirectView,
)
from core_explore_keyword_app.components.search_operator import (
    api as search_operator_api,
)
from core_explore_keyword_app.views.user.views import KeywordSearchView
from core_explore_periodic_table_app.components.persistent_query_periodic_table import (
    api as persistent_query_periodic_table_api,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)
from core_explore_periodic_table_app.components.search_operator_mapping import (
    api as search_operator_mapping_api,
)
from core_explore_periodic_table_app.permissions import rights
from core_explore_periodic_table_app.views.user.form import PeriodicTableForm
from core_main_app.commons.exceptions import DoesNotExist
from core_main_app.components.template import api as template_api
from core_main_app.settings import DATA_SORTING_FIELDS
from core_main_app.utils.rendering import render


class PeriodicTableBuildQueryView(KeywordSearchView):
    """Periodic Table Build Query View"""

    results_url = "core_explore_periodic_table_results"
    query_builder_interface = (
        "core_explore_periodic_table_app/user/periodic_table/periodic.html"
    )

    @method_decorator(
        decorators.permission_required(
            content_type=rights.EXPLORE_PERIODIC_TABLE_CONTENT_TYPE,
            permission=rights.EXPLORE_PERIODIC_TABLE_ACCESS,
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

        # Set page title
        context.update({"page_title": "Search By Periodic Table"})

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
            query = query_api.create_default_query(request, [])
            # upsert the query
            query_api.upsert(query, request.user)
            # create all data for select values in forms
            periodic_table_data_form = {
                "query_id": str(query.id),
                "user_id": query.user_id,
            }
        else:  # query_id is not None
            try:
                # get the query id
                query = query_api.get_by_id(query_id, request.user)
                user_id = query.user_id

                # get all elements back
                elements = self._parse_query(query.content)

                # get all version managers
                version_managers = []
                for template in query.templates.all():
                    version_managers.append(str(template.version_manager.id))
                # create all data for select values in forms
                periodic_table_data_form = {
                    "query_id": str(query.id),
                    "user_id": user_id,
                    "elements": elements,
                    "global_templates": version_managers,
                    "order_by_field": super().build_sorting_context_array(
                        query
                    ),
                    "user_templates": version_managers,
                }
                # set the correct ordering for the context
                if periodic_table_data_form["order_by_field"] != 0:
                    default_order = periodic_table_data_form["order_by_field"]
            except Exception as exception:
                error = "An unexpected error occurred while loading the query: {}.".format(
                    str(exception)
                )
                return {"error": error}

        search_form = PeriodicTableForm(
            data=periodic_table_data_form, request=request
        )
        return self._format_keyword_search_context(
            search_form, error, None, default_order
        )

    @method_decorator(
        decorators.permission_required(
            content_type=rights.EXPLORE_PERIODIC_TABLE_CONTENT_TYPE,
            permission=rights.EXPLORE_PERIODIC_TABLE_ACCESS,
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

        # Set page title
        context.update({"page_title": "Search By Periodic Table"})

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
        search_form = PeriodicTableForm(data=request.POST, request=request)
        # validate form
        if search_form.is_valid():
            try:
                # get form values
                query_id = search_form.cleaned_data.get("query_id", None)
                elements = search_form.cleaned_data.get("elements", None)
                global_templates = search_form.cleaned_data.get(
                    "global_templates", []
                )
                user_templates = search_form.cleaned_data.get(
                    "user_templates", []
                )
                order_by_field_array = (
                    search_form.cleaned_data.get("order_by_field", "")
                    .strip()
                    .split(";")
                )
                # get all template version manager ids
                template_version_manager_ids = (
                    global_templates + user_templates
                )
                # from ids, get all version manager
                version_manager_list = (
                    template_version_manager_api.get_by_id_list(
                        template_version_manager_ids, request=request
                    )
                )
                # from all version manager, build a list of all version (template)
                template_ids = []
                list(
                    [
                        template_ids.extend(x.versions)
                        for x in version_manager_list
                    ]
                )
                if query_id is None or elements is None:
                    error = "Expected parameters are not provided"
                else:
                    # get query
                    query = query_api.get_by_id(query_id, request.user)
                    if len(query.data_sources) == 0:
                        warning = "Please select at least 1 data source."
                    else:
                        # update query
                        query.templates.set(
                            template_api.get_all_accessible_by_id_list(
                                template_ids, request=request
                            )
                        )

                        try:
                            element_search_operators = (
                                self._format_keyword_to_search_operators(
                                    elements.split(",")
                                )
                            )
                        except Exception as ex:
                            warning = str(ex)
                            element_search_operators = ""

                        query.content = self._build_query(
                            element_search_operators
                        )
                        # set the data-sources filter value according to the POST request field
                        for data_sources_index in range(
                            len(query.data_sources)
                        ):
                            # update the data-source filter only if it's not a new data-source
                            # (the default filter value is already added when the data-source
                            # is created)
                            if data_sources_index in range(
                                0, len(order_by_field_array)
                            ):
                                query.data_sources[data_sources_index][
                                    "order_by_field"
                                ] = order_by_field_array[data_sources_index]

                        query_api.upsert(query, request.user)
            except DoesNotExist as does_not_exist_error:
                error = (
                    str(does_not_exist_error)
                    if does_not_exist_error
                    else "An unexpected error occurred while retrieving the query."
                )
            except Exception as exception:
                error = "An unexpected error occurred: {}.".format(
                    str(exception)
                )
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

        Returns:
            - Search operator list (ex.["so1:Au", "so2:Au", "so1:U", "so2:U"])
            - Empty list if the query is empty
        """
        result = []
        all_so_mapping = search_operator_mapping_api.get_all()

        if all_so_mapping.count() > 0:
            for so_mapping in all_so_mapping:
                search_operator = search_operator_api.get_by_id(
                    str(so_mapping.search_operator.id)
                )
                for element in elements_list:
                    element and result.append(
                        f"{search_operator.name}:{element}"
                    )
        else:
            raise Exception(
                "No search operators has been configured, please contact an administrator."
            )

        return result

    @staticmethod
    def get_description():
        """Get the description page

        Returns:

        """
        return (
            "Click on an element of the Periodic Table to add it to your query. "
            "You can save queries and you will retrieve them on your next connection. "
            "When your query is done, please click on Submit Query to get XML documents"
            " that match the criteria."
        )

    @staticmethod
    def get_title():
        """Get the title page

        Returns:

        """
        return "Periodic Table"


class ResultQueryRedirectPeriodicSearchView(ResultQueryRedirectView):
    """Result Query Redirect Periodic Search View"""

    model_name = PersistentQueryPeriodicTable.__name__
    object_name = "persistent_query_periodic_table"
    redirect_url = "core_explore_periodic_table_index"

    @method_decorator(
        decorators.permission_required(
            content_type=rights.EXPLORE_PERIODIC_TABLE_CONTENT_TYPE,
            permission=rights.EXPLORE_PERIODIC_TABLE_ACCESS,
        )
    )
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    @staticmethod
    def _get_persistent_query_by_id(persistent_query_id, user):
        return persistent_query_periodic_table_api.get_by_id(
            persistent_query_id, user
        )

    @staticmethod
    def _get_persistent_query_by_name(persistent_query_name, user):
        return persistent_query_periodic_table_api.get_by_name(
            persistent_query_name, user
        )

    @staticmethod
    def get_url_path():
        return reverse(
            ResultQueryRedirectPeriodicSearchView.redirect_url,
            kwargs={"query_id": "query_id"},
        ).split("query_id")[0]

    @staticmethod
    def _get_reversed_url(query):
        return reverse(
            ResultQueryRedirectPeriodicSearchView.redirect_url,
            kwargs={"query_id": query.id},
        )

    @staticmethod
    def _get_reversed_url_if_failed():
        return reverse("core_explore_periodic_table_index")
