""" Auto discovery of Periodic Table
"""
from os.path import join

from django.contrib.staticfiles import finders
from django.http.request import HttpRequest

import core_composer_app.components.type_version_manager.api as type_version_manager_api
import core_explore_example_app.components.explore_data_structure.api as explore_data_structure_api
import core_explore_periodic_table_app.components.periodic_table_type.api as periodic_table_type_api
from core_composer_app.components.type.models import Type
from core_composer_app.components.type_version_manager.models import TypeVersionManager
from core_explore_periodic_table_app.components.periodic_table_type.models import PeriodicTableType

XSD_FILENAME = 'default_chemical_element_type.xsd'


def discover_periodic_table(app_name):
    """ Periodic Table discover

    Returns:

    """
    try:
        # get all type link to the periodic table search (should have 0 or 1 element)
        periodic_table_type_list = periodic_table_type_api.get_all()

        # if no file is linked
        if len(periodic_table_type_list) == 0:
            # we link one by default
            url_file = finders.find(join('core_explore_periodic_table_app', 'common', 'xsd', XSD_FILENAME))
            with open(url_file, 'r') as chemical_elements_file:
                xsd_chemical_elements = chemical_elements_file.read()

            # Create the new version manager
            type_object = Type(filename=XSD_FILENAME, content=xsd_chemical_elements)
            type_version_manager = TypeVersionManager(title='default_chemical_element_type')
            type_version_manager = type_version_manager_api.insert(type_version_manager, type_object, [])

            # Insert the configuration
            periodic_table_type = PeriodicTableType(type_version_manager)
            periodic_table_type_api.upsert(periodic_table_type)

            # TODO: Remove this mocked request once the parser does not use sessions.
            request = HttpRequest()
            request.session = dict()
            # Generate relative data structure
            explore_data_structure_api.create_and_get_explore_data_structure(request,
                                                                             type_version_manager.current,
                                                                             app_name)
    except Exception, e:
        print(e.message)
