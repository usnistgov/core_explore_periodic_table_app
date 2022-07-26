""" Custom admin site for the Persistent Query Periodic Table model
"""
from django.contrib import admin


class CustomPersistentQueryPeriodicTableAdmin(admin.ModelAdmin):
    """CustomPersistentQueryPeriodicTableAdmin"""

    exclude = ["data_sources"]

    def has_add_permission(self, request, obj=None):
        """Prevent from manually adding Persistent Queries"""
        return False
