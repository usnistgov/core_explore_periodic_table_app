""" Discover rules for core explore periodic table app.
"""
import logging

from core_explore_periodic_table_app.permissions import (
    rights as explore_periodic_table_rights,
)
from core_main_app.permissions import rights as main_rights

logger = logging.getLogger(__name__)


def init_permissions(apps):
    """Initialization of groups and permissions.

    Args:
        apps (Apps): List of applications to init
    """
    try:
        group = apps.get_model("auth", "Group")
        permission = apps.get_model("auth", "Permission")

        # Get or Create the default group
        default_group, created = group.objects.get_or_create(
            name=main_rights.DEFAULT_GROUP
        )

        # Get explore periodic table permissions
        explore_access_perm = permission.objects.get(
            codename=explore_periodic_table_rights.EXPLORE_PERIODIC_TABLE_ACCESS
        )

        # Add permissions to default group
        default_group.permissions.add(explore_access_perm)
    except Exception as exception:
        logger.error(
            "Impossible to init explore_periodic_table permissions: %s",
            str(exception),
        )
