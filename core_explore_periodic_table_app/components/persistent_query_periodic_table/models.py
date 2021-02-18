""" Persistent Query Periodic table model
"""
from mongoengine import errors as mongoengine_errors

from core_explore_common_app.components.abstract_persistent_query.models import (
    AbstractPersistentQuery,
)
from core_main_app.commons import exceptions


class PersistentQueryPeriodicTable(AbstractPersistentQuery):
    """Persistent Query Periodic Table"""

    @staticmethod
    def get_by_id(query_id):
        """Get a persistent query periodic table

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

    @staticmethod
    def get_by_name(query_name):
        """Get a persistent query periodic table

        Args:
            query_name:

        Returns:

        """
        try:
            return PersistentQueryPeriodicTable.objects().get(name=query_name)
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as e:
            raise exceptions.ModelError(str(e))

    @staticmethod
    def get_all():
        """Return all persistent query periodic table.

        Returns:

        """
        return PersistentQueryPeriodicTable.objects.all()

    @staticmethod
    def get_all_by_user(user_id):
        """Return all persistent query periodic table by user.


        Args:
            user_id:

        Returns:

        """
        return PersistentQueryPeriodicTable.objects(user_id=str(user_id))

    @staticmethod
    def get_none():
        """Return None object, used by data.

        Returns:

        """
        return PersistentQueryPeriodicTable.objects().none()
