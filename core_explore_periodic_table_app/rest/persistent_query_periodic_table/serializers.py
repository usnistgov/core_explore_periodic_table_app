""" Serializers used for the persistent query periodic table REST API.
"""
from rest_framework_mongoengine.serializers import DocumentSerializer

from core_explore_periodic_table_app.components.persistent_query_periodic_table import (
    api as persistent_query_periodic_table_api,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)


class PersistentQueryPeriodicTableSerializer(DocumentSerializer):
    """Persistent query periodic_table"""

    class Meta(object):
        model = PersistentQueryPeriodicTable
        fields = ["id", "user_id", "content", "templates", "name"]
        read_only_fields = ("id", "user_id")

    def create(self, validated_data):
        """Create and return a new `PersistentQueryPeriodicTable` instance, given the validated data."""

        # Create instance from the validated data and insert it in DB
        persistent_query_periodic_table = PersistentQueryPeriodicTable(
            user_id=str(self.context["request"].user.id),
            content=validated_data["content"] if "content" in validated_data else None,
            templates=validated_data["templates"]
            if "templates" in validated_data
            else None,
            name=validated_data["name"] if "name" in validated_data else None,
        )
        return persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, self.context["request"].user
        )

    # Update instance from the validated data and insert it in DB
    def update(self, persistent_query_periodic_table, validated_data):
        """Update and return an existing `PersistentQueryPeriodicTable` instance, given the validated
        data.
        """
        persistent_query_periodic_table.content = validated_data.get(
            "content", persistent_query_periodic_table.content
        )
        persistent_query_periodic_table.templates = validated_data.get(
            "templates", persistent_query_periodic_table.templates
        )
        persistent_query_periodic_table.name = validated_data.get(
            "name", persistent_query_periodic_table.name
        )
        return persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, self.context["request"].user
        )


class PersistentQueryPeriodicTableAdminSerializer(DocumentSerializer):
    """PersistentQueryAdminPeriodicTable Serializer"""

    class Meta(object):
        """Meta"""

        model = PersistentQueryPeriodicTable
        fields = ["id", "user_id", "content", "templates", "name"]

    def create(self, validated_data):
        """
        Create and return a new `PersistentQueryPeriodicTable` instance, given the validated data.
        """
        # Create data
        persistent_query_periodic_table = PersistentQueryPeriodicTable(
            user_id=validated_data["user_id"],
            content=validated_data["content"] if "content" in validated_data else None,
            templates=validated_data["templates"]
            if "templates" in validated_data
            else None,
            name=validated_data["name"] if "name" in validated_data else None,
        )
        return persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, self.context["request"].user
        )
