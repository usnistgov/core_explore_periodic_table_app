""" PeriodicTableType api
"""
from core_explore_periodic_table_app.components.search_operator_mapping.models import (
    SearchOperatorMapping,
)


def get_all():
    """Return all PeriodicTableType.

    Returns: PeriodicTableType collection
    """
    return SearchOperatorMapping.get_all()


def get_by_id(pk):
    """Get mapping by search operator mapping id

    Args:
        pk:

    Returns:

    """
    return SearchOperatorMapping.get_by_id(pk=pk)


def get_by_search_operator_id(search_operator_id):
    """Get mapping by search operator id

    Args:
        search_operator_id:

    Returns:

    """
    return SearchOperatorMapping.get_by_search_operator_id(
        search_operator_id=search_operator_id
    )


def upsert(search_operator_mapping):
    """Insert or update an search operator mapping

    Args:
        search_operator_mapping:

    Returns:

    """
    search_operator_mapping.save()
    return search_operator_mapping


def delete(search_operator_mapping):
    """Delete a mapping.

    Args:
         search_operator_mapping:

    Returns:
    """
    search_operator_mapping.delete()
