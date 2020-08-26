""" Periodic Table Model
"""
from django_mongoengine import fields, Document
from mongoengine import CASCADE

from core_explore_keyword_app.components.search_operator.models import SearchOperator


class SearchOperatorMapping(Document):
    """Periodic Table Type configuration object"""

    search_operator = fields.ReferenceField(
        SearchOperator,
        reverse_delete_rule=CASCADE,
        blank=False,
    )

    @staticmethod
    def get_all():
        """Get all SearchOperatorMapping.

        Args:

        Returns:

        """
        return SearchOperatorMapping.objects().all()

    @staticmethod
    def get_by_id(pk):
        """Get search operator mapping by id

        Args:
            pk:

        Returns:

        """
        return SearchOperatorMapping.objects.get(pk=str(pk))

    @staticmethod
    def get_by_search_operator_id(search_operator_id):
        """Get mapping by search operator id

        Args:
            search_operator_id:

        Returns:

        """
        return SearchOperatorMapping.objects(search_operator=str(search_operator_id))
