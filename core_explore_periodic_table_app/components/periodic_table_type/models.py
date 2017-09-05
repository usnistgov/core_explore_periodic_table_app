""" Periodic Table Model
"""
from django_mongoengine import fields, Document
from core_composer_app.components.type_version_manager.models import TypeVersionManager


class PeriodicTableType(Document):
    """ Periodic Table Type configuration object
    """
    type_version_manager = fields.ReferenceField(TypeVersionManager)

    @staticmethod
    def get_all():
        """ Get all PeriodicTableType.

        Args:

        Returns:

        """
        return PeriodicTableType.objects().all()

    @staticmethod
    def get_first():
        """ Get the first PeriodicTableType.

        Args:

        Returns:

        """
        return PeriodicTableType.get_all().first()
