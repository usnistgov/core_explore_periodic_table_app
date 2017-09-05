""" Explore Periodic table app Ajax views
"""
import json

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator

import core_explore_example_app.components.saved_query.api as saved_query_api
import core_explore_example_app.permissions.rights as rights
import core_explore_periodic_table_app.components.periodic_table_type.api as periodic_table_type_api
import core_main_app.components.template.api as template_api
import core_main_app.utils.decorators as decorators
from core_explore_common_app.components.query import api as query_api
from core_explore_example_app.components.saved_query.models import SavedQuery
from core_explore_example_app.views.user.ajax import SaveQueryView
from core_explore_periodic_table_app.utils.displayed_query import fields_to_pretty_query
from core_explore_periodic_table_app.utils.mongo_query import fields_to_query, get_type_name


@decorators.permission_required(content_type=rights.explore_example_content_type,
                                permission=rights.explore_example_access, raise_exception=True)
def get_query_values(request):
    """ Get all values from a query

    Args:
        request:

    Returns:

    """
    saved_query_id = request.GET.get('savedQueryID', None)

    if saved_query_id is not None:
        # get the same query
        saved_query = saved_query_api.get_by_id(saved_query_id.replace('query', ''))
        query = json.loads(saved_query.query)
        values = set()
        _get_values_from_json_query(values, query)
    return HttpResponse(json.dumps(list(values)), content_type='application/javascript')


@decorators.permission_required(content_type=rights.explore_example_content_type,
                                permission=rights.explore_example_access, raise_exception=True)
def submit_query(request):
    """ Submit a query

    Args:
        request:

    Returns:

    """
    try:
        query_id = request.POST['queryID']
        selected_values = json.loads(request.POST.get('selectedValues', None))

        errors = []
        if len(selected_values) == 0:
            errors.append('Select at least one element<br/>')

        query_object = query_api.get_by_id(query_id)
        if len(query_object.data_sources) == 0:
            errors.append("Please select at least 1 data source.")

        if len(errors) == 0:
            # Get the path from this data structure (here it's the name of the option)
            query_content = fields_to_query(selected_values)
            query_object.content = json.dumps(query_content)
            query_api.upsert(query_object)
        else:
            return HttpResponseBadRequest(errors, content_type='application/javascript')

        return HttpResponse(json.dumps({}), content_type='application/javascript')
    except Exception, e:
        return HttpResponseBadRequest(e.message, content_type='application/javascript')


class PeriodicTableSaveQueryView(SaveQueryView):
    fields_to_query_func = None

    @method_decorator(decorators.
                      permission_required(content_type=rights.explore_example_content_type,
                                          permission=rights.explore_example_save_query,
                                          raise_exception=True))
    def post(self, request):
        """Save a query and update the html display

        Args:
            request:

        Returns:

        """
        # Check that the user can save a query
        if '_auth_user_id' not in request.session:
            return HttpResponseBadRequest('You have to login to save a query.', content_type='application/javascript')

        try:
            # Get selected values from the periodic table
            periodic_table_values = json.loads(request.POST.get('periodic_table_values', None))

            # Get the template id linked to the periodic table
            template_id = periodic_table_type_api.get_first().type_version_manager.current

            query = self.fields_to_query_func(periodic_table_values)
            displayed_query = fields_to_pretty_query(periodic_table_values, "Element")

            # save the query in the data base
            saved_query = SavedQuery(user_id=str(request.user.id),
                                     template=template_api.get(template_id),
                                     query=json.dumps(query),
                                     displayed_query=displayed_query)
            saved_query_api.upsert(saved_query)
        except Exception as e:
            return HttpResponseBadRequest(e.message, content_type='application/javascript')
        return HttpResponse(json.dumps({}), content_type='application/javascript')


def _get_values_from_json_query(return_value_list, json_query):
    """ Get all values from json query

    Args:
        return_value_list:
        json_query:

    Returns:

    """
    for key, value in json_query.iteritems():
        if key == "$and" or key == "$or":
            for item in value:
                _get_values_from_json_query(return_value_list, item)
        if key == "value":
            return_value_list.add(value)

