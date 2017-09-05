""" Periodic table's views
"""

import core_explore_periodic_table_app.components.periodic_table_type.api as periodic_table_type_api
from core_explore_example_type_app.views.user.views import TypeBuildQueryView


class PeriodicTableBuildQueryView(TypeBuildQueryView):
    save_query_url = 'core_explore_periodic_table_save_query'
    results_url = 'core_explore_periodic_table_results'
    data_sources_selector_template = 'core_explore_periodic_table_app/user/selector/data_sources_selector.html'
    query_builder_interface = 'core_explore_periodic_table_app/user/periodic_table/periodic.html'

    def get(self, request, template_id=None, query_id=None):
        """ Get the Periodic Table Build query view (Index)

        Args:
            request:
            template_id:
            query_id:

        Returns:

        """
        if template_id is None:
            periodic_table_type = periodic_table_type_api.get_first()
            template_id = periodic_table_type.type_version_manager.current
        return super(PeriodicTableBuildQueryView, self).get(request, template_id, query_id)

    @staticmethod
    def _get_css():
        """ Get and override css list

        Returns:

        """
        base_css = super(PeriodicTableBuildQueryView, PeriodicTableBuildQueryView)._get_css()
        # Add custom css
        base_css.extend(['core_explore_periodic_table_app/user/css/periodic_table/periodic.css'])
        return base_css

    @staticmethod
    def _get_js():
        """ Get and override js list

        Returns:

        """
        base_js = super(PeriodicTableBuildQueryView, PeriodicTableBuildQueryView)._get_js()
        # Add custom js
        base_js.extend([{
            "path": 'core_explore_periodic_table_app/user/js/periodic_table/periodic.js'
        }])
        return base_js

    @staticmethod
    def get_description():
        """ Get the description page

        Returns:

        """
        return "Click on an element of the Periodic Table to add it to your query. " \
               "You can save queries and you will retrieve them on your next connection. " \
               "When your query is done, please click on Submit Query to get XML documents that match the criteria."

    @staticmethod
    def get_title():
        """ Get the title page

        Returns:

        """
        return "Periodic Table"
