"""Serializers used throughout the Search operator mapping Rest API
"""
from rest_framework.exceptions import ValidationError
from rest_framework_mongoengine.serializers import DocumentSerializer

from core_explore_keyword_app.components.search_operator import (
    api as search_operator_api,
)
from core_explore_periodic_table_app.components.search_operator_mapping import (
    api as search_operator_mapping_api,
)
from core_explore_periodic_table_app.components.search_operator_mapping.models import (
    SearchOperatorMapping,
)
from core_main_app.commons.exceptions import DoesNotExist


class SearchOperatorMappingSerializer(DocumentSerializer):
    """SearchOperatorMapping serializer"""

    class Meta(object):
        """Meta"""

        model = SearchOperatorMapping
        fields = [
            "id",
            "search_operator",
        ]
        read_only_fields = ("id",)

    def create(self, validated_data):
        """Create and return a new `SearchOperatorMapping` instance."""

        new_search_operator_id = validated_data["search_operator"]

        # Create instance from the validated data and insert it in DB
        instance = SearchOperatorMapping(search_operator=new_search_operator_id)
        search_operator_mapping_api.upsert(instance)

        return instance

    def update(self, instance, validated_data):
        """Update and return an existing `SearchOperatorMapping` instance."""

        new_search_operator_id = validated_data.get(
            "search_operator", instance.search_operator
        )

        instance.search_operator = new_search_operator_id

        return search_operator_mapping_api.upsert(instance)
