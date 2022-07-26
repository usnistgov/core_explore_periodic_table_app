""" Custom admin site for the Search Operator Mapping model
"""
from django.contrib import admin


class CustomSearchOperatorMappingAdmin(admin.ModelAdmin):
    """CustomSearchOperatorMappingAdmin"""

    def has_add_permission(self, request, obj=None):
        """Prevent from manually adding Search Operator Mapping"""
        return False
