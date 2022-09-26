""" Persistent Query Periodic table model
"""

from django.core.exceptions import ObjectDoesNotExist

from core_explore_common_app.components.abstract_persistent_query.models import (
    AbstractPersistentQuery,
)
from core_main_app.commons import exceptions


class PersistentQueryPeriodicTable(AbstractPersistentQuery):
    """Persistent Query Periodic Table"""

    class Meta:
        """Meta"""

        verbose_name = "Persistent Query by Periodic Table"
        verbose_name_plural = "Persistent Queries by Periodic Table"

    @staticmethod
    def get_by_id(query_id):
        """Get a persistent query periodic table

        Args:
            query_id:

        Returns:

        """
        try:
            return PersistentQueryPeriodicTable.objects.get(pk=query_id)
        except ObjectDoesNotExist as exception:
            raise exceptions.DoesNotExist(str(exception))
        except Exception as exception:
            raise exceptions.ModelError(str(exception))

    @staticmethod
    def get_by_name(query_name):
        """Get a persistent query periodic table

        Args:
            query_name:

        Returns:

        """
        try:
            return PersistentQueryPeriodicTable.objects.get(name=query_name)
        except ObjectDoesNotExist as exception:
            raise exceptions.DoesNotExist(str(exception))
        except Exception as exception:
            raise exceptions.ModelError(str(exception))

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
        return PersistentQueryPeriodicTable.objects.filter(
            user_id=str(user_id)
        ).all()

    @staticmethod
    def get_none():
        """Return None object, used by data.

        Returns:

        """
        return PersistentQueryPeriodicTable.objects.none()
