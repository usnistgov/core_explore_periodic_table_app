""" Core Periodic table apps config
"""
from django.apps import AppConfig
from core_explore_periodic_table_app import discover


class CoreExplorePeriodicTableAppConfig(AppConfig):
    """ Periodic Table configuration
    """
    name = 'core_explore_periodic_table_app'
    verbose_name = "Core Periodic table App Config"

    def ready(self):
        """ Run once at startup
        """
        discover.discover_periodic_table(self.name)
