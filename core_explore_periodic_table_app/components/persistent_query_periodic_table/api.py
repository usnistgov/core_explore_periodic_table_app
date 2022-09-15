""" Persistent Query Periodic table API
"""

from core_explore_common_app.access_control.api import (
    can_read_persistent_query,
    can_write_persistent_query,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)
from core_main_app.access_control.api import has_perm_administration
from core_main_app.access_control.decorators import access_control


@access_control(can_write_persistent_query)
def upsert(persistent_query_periodic_table, user):
    """Saves or update persistent query

    Args:
        persistent_query_periodic_table:
        user:

    Returns:

    """
    persistent_query_periodic_table.save()
    return persistent_query_periodic_table


@access_control(can_read_persistent_query)
def get_by_id(persistent_query_periodic_table_id, user):
    """Return the Persistent Query Periodic Table with the given id

    Args:
        persistent_query_periodic_table_id:
        user:

    Returns:

    """
    return PersistentQueryPeriodicTable.get_by_id(persistent_query_periodic_table_id)


@access_control(can_read_persistent_query)
def get_by_name(persistent_query_periodic_table_name, user):
    """Return the Persistent Query Periodic Table with the given name

    Args:
        persistent_query_periodic_table_name:
        user:
    Returns:

    """
    return PersistentQueryPeriodicTable.get_by_name(
        persistent_query_periodic_table_name
    )


@access_control(can_write_persistent_query)
def delete(persistent_query_periodic_table, user):
    """Deletes the Persistent Query Periodic Table and the element associated

    Args:
        persistent_query_periodic_table:
        user:
    """
    persistent_query_periodic_table.delete()


@access_control(can_write_persistent_query)
def set_name(persistent_query_periodic_table, name, user):
    """Set name to Persistent Query Periodic Table

    Args:
        persistent_query_periodic_table:
        name:
        user:
    """
    persistent_query_periodic_table.name = name
    persistent_query_periodic_table.save()


@access_control(has_perm_administration)
def get_all(user):
    """get all Persistent Query Periodic Table

    Args:
        user:
    """
    return PersistentQueryPeriodicTable.get_all()


@access_control(can_read_persistent_query)
def get_all_by_user(user):
    """get persistent Query Periodic Table by user

    Args:
        user:
    """
    return PersistentQueryPeriodicTable.get_all_by_user(user.id)
