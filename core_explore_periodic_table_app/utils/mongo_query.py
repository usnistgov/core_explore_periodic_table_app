"""Util to build queries for mongo db
"""
import core_explore_example_app.components.explore_data_structure.api as explore_data_structure_api
import core_explore_periodic_table_app.components.periodic_table_type.api as periodic_table_type_api
from core_explore_example_app.utils import mongo_query as common_mongo_query
from core_explore_periodic_table_app.apps import CoreExplorePeriodicTableAppConfig


def fields_to_query(values):
    """ Takes values from the periodic table and creates a query from them

    Args:
        values:

    Returns:

    """
    query = dict()
    path = get_type_name()
    # build the query
    for value in values:
        criteria = common_mongo_query.build_criteria(path, "is", value, path, "xsd", is_not=False, use_wildcard=True)
        if values.index(value) == 0:
            query.update(criteria)
        else:
            query = common_mongo_query.build_and_criteria(query, criteria)
    return query


def get_type_name():
    """ Get path form periodic table type

    Returns:

    """
    # Get the template id linked to the periodic table
    template_id = periodic_table_type_api.get_first().type_version_manager.current
    # Get the template's data structure
    explore_data_structure = explore_data_structure_api. \
        get_by_user_id_and_template_id(CoreExplorePeriodicTableAppConfig.name,
                                       template_id)

    # Get the path from this data structure (here it's the name of the option)
    return explore_data_structure.data_structure_element_root.options['name']