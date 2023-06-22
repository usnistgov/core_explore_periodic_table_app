""" core explore periodic table admin views
"""
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import HttpResponseBadRequest

from core_explore_keyword_app.components.search_operator import (
    api as search_operator_api,
)
from core_explore_periodic_table_app.components.search_operator_mapping import (
    api as search_operator_mapping_api,
)
from core_explore_periodic_table_app.components.search_operator_mapping.models import (
    SearchOperatorMapping,
)
from core_explore_periodic_table_app.views.admin.forms import (
    AssociatedPeriodicTableSearchOperatorForm,
)
from core_main_app.utils.rendering import admin_render


@staff_member_required
def manage_periodic_table_index(request):
    """Index admin view

    Args:
        request:

    Returns:

    """
    try:
        if request.method == "POST":
            return _manage_periodic_table_index_post(request)

        return _manage_periodic_table_index_get(request)
    except Exception as exception:
        return HttpResponseBadRequest(str(exception))


def _manage_periodic_table_index_get(request):
    """Index admin view GET

    Args:
        request:

    Returns:

    """
    # load the form
    associated_form = AssociatedPeriodicTableSearchOperatorForm()
    assets = {"css": ["core_explore_periodic_table_app/admin/form.css"]}

    context = {"associated_form": associated_form}

    return admin_render(
        request,
        "core_explore_periodic_table_app/admin/periodic_table_type/manage_periodic_table_type.html",
        context=context,
        assets=assets,
    )


def _manage_periodic_table_index_post(request):
    """Index admin view POST

    Args:
        request:

    Returns:

    """
    # get the new id
    selected_search_operator_list = request.POST.getlist(
        "search_operator_list"
    )
    search_operator_mapping = list(search_operator_mapping_api.get_all())
    search_operator_list = list(search_operator_api.get_all())

    for search_operator in search_operator_list:
        find_in_mapping = next(
            (
                x
                for x in search_operator_mapping
                if x.search_operator.id == search_operator.id
            ),
            None,
        )
        find_in_selected = next(
            (
                y
                for y in selected_search_operator_list
                if y == str(search_operator.id)
            ),
            None,
        )
        if find_in_mapping and not find_in_selected:
            # delete the mapping
            current_search_operator_mapping = (
                search_operator_mapping_api.get_by_search_operator_id(
                    search_operator.id
                )
            )
            search_operator_mapping_api.delete(current_search_operator_mapping)
        elif not find_in_mapping and find_in_selected:
            # add the mapping
            search_operator_mapping_api.upsert(
                SearchOperatorMapping(search_operator=search_operator)
            )

    # load the form
    associated_form = AssociatedPeriodicTableSearchOperatorForm()
    assets = {"css": ["core_explore_periodic_table_app/admin/form.css"]}

    context = {"associated_form": associated_form}

    messages.add_message(
        request, messages.SUCCESS, "Information saved with success."
    )

    return admin_render(
        request,
        "core_explore_periodic_table_app/admin/periodic_table_type/manage_periodic_table_type.html",
        context=context,
        assets=assets,
    )
