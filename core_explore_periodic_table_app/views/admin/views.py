""" core explore periodic table admin views
"""

from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import HttpResponseBadRequest

import core_explore_example_app.components.explore_data_structure.api as explore_data_structure_api
import core_explore_periodic_table_app.components.periodic_table_type.api as periodic_table_type_api
import core_main_app.components.version_manager.api as version_manager_api
from core_explore_periodic_table_app.apps import CoreExplorePeriodicTableAppConfig
from core_explore_periodic_table_app.views.admin.forms import AssociatedPeriodicTableTypeForm
from core_main_app.utils.rendering import admin_render


@staff_member_required
def manage_periodic_table_index(request):
    """ Index admin view

    Args:
        request:

    Returns:

    """
    try:
        if request.method == 'POST':
            return _manage_periodic_table_index_post(request)
        else:
            return _manage_periodic_table_index_get(request)
    except Exception as e:
        return HttpResponseBadRequest(e.message)


def _manage_periodic_table_index_get(request):
    """ Index admin view GET

    Args:
        request:

    Returns:

    """
    # load the form
    periodic_table_type = periodic_table_type_api.get_first()
    data_form = {'types_manager': periodic_table_type.type_version_manager.id}
    associated_form = AssociatedPeriodicTableTypeForm(data_form)

    context = {
        'associated_form': associated_form
    }

    return admin_render(request,
                        'core_explore_periodic_table_app/admin/periodic_table_type/manage_periodic_table_type.html',
                        context=context)


def _manage_periodic_table_index_post(request):
    """ Index admin view POST

    Args:
        request:

    Returns:

    """
    # get the new id
    type_manager_id = request.POST.get('types_manager', None)

    if type_manager_id is not None:
        # get the version manager
        version_manager = version_manager_api.get(type_manager_id)
        # upsert the periodic table type
        periodic_table_type = periodic_table_type_api.get_first()
        periodic_table_type.type_version_manager = version_manager
        periodic_table_type_api.upsert(periodic_table_type)
        # create linked data structure
        explore_data_structure_api.create_and_get_explore_data_structure(request,
                                                                         version_manager.current,
                                                                         CoreExplorePeriodicTableAppConfig.name)

    return _manage_periodic_table_index_get(request)
