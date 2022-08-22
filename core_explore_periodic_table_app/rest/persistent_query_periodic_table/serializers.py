""" Serializers used for the persistent query periodic table REST API.
"""
from rest_framework.serializers import ModelSerializer

from core_explore_periodic_table_app.components.persistent_query_periodic_table import (
    api as persistent_query_periodic_table_api,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)


class PersistentQueryPeriodicTableSerializer(ModelSerializer):
    """Persistent query periodic_table"""

    class Meta:
        """Meta"""

        model = PersistentQueryPeriodicTable
        fields = ["id", "user_id", "content", "templates", "name"]
        read_only_fields = ("id", "user_id")

    def create(self, validated_data):
        """Create and return a new `PersistentQueryPeriodicTable` instance, given the validated data."""

        # Create instance from the validated data and insert it in DB
        persistent_query_periodic_table = PersistentQueryPeriodicTable(
            user_id=str(self.context["request"].user.id),
            content=validated_data["content"] if "content" in validated_data else None,
            name=validated_data["name"] if "name" in validated_data else None,
        )

        persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, self.context["request"].user
        )
        if "templates" in validated_data:
            persistent_query_periodic_table.templates.set(validated_data["templates"])

        return persistent_query_periodic_table

    # Update instance from the validated data and insert it in DB
    def update(self, persistent_query_periodic_table, validated_data):
        """Update and return an existing `PersistentQueryPeriodicTable` instance, given the validated
        data.
        """
        persistent_query_periodic_table.content = validated_data.get(
            "content", persistent_query_periodic_table.content
        )
        persistent_query_periodic_table.name = validated_data.get(
            "name", persistent_query_periodic_table.name
        )
        persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, self.context["request"].user
        )
        if "templates" in validated_data:
            persistent_query_periodic_table.templates.set(validated_data["templates"])
        return persistent_query_periodic_table


class PersistentQueryPeriodicTableAdminSerializer(ModelSerializer):
    """PersistentQueryAdminPeriodicTable Serializer"""

    class Meta:
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
            name=validated_data["name"] if "name" in validated_data else None,
        )
        persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, self.context["request"].user
        )
        if "templates" in validated_data:
            persistent_query_periodic_table.templates.set(validated_data["templates"])
        return persistent_query_periodic_table
