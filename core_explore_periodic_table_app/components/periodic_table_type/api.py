""" PeriodicTableType api
"""
from core_explore_periodic_table_app.components.periodic_table_type.models import PeriodicTableType


def get_all():
    """ Return all PeriodicTableType.

        Returns: PeriodicTableType collection
    """
    return PeriodicTableType.get_all()


def get_first():
    """ Return the first PeriodicTableType

    Returns: PeriodicTableType object

    """
    return PeriodicTableType.get_first()


def upsert(periodic_table_type):
    """ Insert or update an periodic table type

    Args:
        periodic_table_type:

    Returns:

    """
    return periodic_table_type.save()
