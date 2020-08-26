""" Persistent Query Periodic table API
"""
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)


def get_by_id(persistent_query_periodic_table_id):
    """Return the Persistent Query Periodic table with the given id

    Args:
        persistent_query_periodic_table_id:

    Returns:

    """
    return PersistentQueryPeriodicTable.get_by_id(persistent_query_periodic_table_id)
