""" Explore Periodic Table models
"""

from django.db import models

from core_explore_periodic_table_app.permissions import rights
from core_main_app.permissions.utils import get_formatted_name


class ExplorePeriodicTable(models.Model):
    class Meta(object):
        verbose_name = "core_explore_periodic_table_app"
        default_permissions = ()
        permissions = (
            (
                rights.explore_periodic_table_access,
                get_formatted_name(rights.explore_periodic_table_access),
            ),
        )
