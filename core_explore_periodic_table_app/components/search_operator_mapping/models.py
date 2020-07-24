""" Periodic Table Model
"""
from django_mongoengine import fields, Document

from core_main_app.utils.validation.regex_validation import not_empty_or_whitespaces


class SearchOperatorMapping(Document):
    """ Periodic Table Type configuration object
    """

    search_operator_id = fields.StringField(
        blank=False, validation=not_empty_or_whitespaces
    )

    @staticmethod
    def get_all():
        """ Get all SearchOperatorMapping.

        Args:

        Returns:

        """
        return SearchOperatorMapping.objects().all()

    @staticmethod
    def get_by_search_operator_id(search_operator_id):
        """ Get mapping by search operator id

        Args:
            search_operator_id:

        Returns:

        """
        return SearchOperatorMapping.objects(search_operator_id=str(search_operator_id))
