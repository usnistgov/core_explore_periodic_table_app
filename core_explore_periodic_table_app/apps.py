""" Core Periodic table apps config
"""
import sys

from django.apps import AppConfig

from core_explore_periodic_table_app.permissions import discover


class CoreExplorePeriodicTableAppConfig(AppConfig):
    """Periodic Table configuration"""

    name = "core_explore_periodic_table_app"
    verbose_name = "Core Explore by Periodic Table App"

    def ready(self):
        """Run when the app is ready.

        Returns:

        """
        if "migrate" not in sys.argv:
            discover.init_permissions(self.apps)
