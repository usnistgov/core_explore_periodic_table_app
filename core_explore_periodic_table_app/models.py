""" Explore Periodic Table models
"""

from django.db import models

from core_main_app.permissions.utils import get_formatted_name
from core_explore_periodic_table_app.permissions import rights


class ExplorePeriodicTable(models.Model):
    """Explore Periodic Table object"""

    class Meta:
        """Meta"""

        verbose_name = "core_explore_periodic_table_app"
        default_permissions = ()
        permissions = (
            (
                rights.EXPLORE_PERIODIC_TABLE_ACCESS,
                get_formatted_name(rights.EXPLORE_PERIODIC_TABLE_ACCESS),
            ),
        )
