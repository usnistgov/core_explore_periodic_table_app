""" Persistent Query Periodic table model
"""
from mongoengine import errors as mongoengine_errors

from core_explore_common_app.components.abstract_persistent_query.models import (
    AbstractPersistentQuery,
)
from core_main_app.commons import exceptions


class PersistentQueryPeriodicTable(AbstractPersistentQuery):
    """Persistent Query Keyword"""

    @staticmethod
    def get_by_id(query_id):
        """Get a persistent query Keyword

        Args:
            query_id:

        Returns:

        """
        try:
            return PersistentQueryPeriodicTable.objects().get(pk=query_id)
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as e:
            raise exceptions.ModelError(str(e))
