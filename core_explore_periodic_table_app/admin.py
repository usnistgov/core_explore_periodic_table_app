"""
Url router for the administration site
"""
from django.contrib import admin
from django.urls import re_path

from core_main_app.admin import core_admin_site
from core_explore_periodic_table_app.components.persistent_query_periodic_table.admin_site import (
    CustomPersistentQueryPeriodicTableAdmin,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)
from core_explore_periodic_table_app.components.search_operator_mapping.admin_site import (
    CustomSearchOperatorMappingAdmin,
)
from core_explore_periodic_table_app.components.search_operator_mapping.models import (
    SearchOperatorMapping,
)
from core_explore_periodic_table_app.views.admin import views as admin_views


admin_urls = [
    re_path(
        r"^periodic_table$",
        admin_views.manage_periodic_table_index,
        name="manage_periodic_table_index",
    ),
]

admin.site.register(SearchOperatorMapping, CustomSearchOperatorMappingAdmin)
admin.site.register(
    PersistentQueryPeriodicTable, CustomPersistentQueryPeriodicTableAdmin
)
urls = core_admin_site.get_urls()
core_admin_site.get_urls = lambda: admin_urls + urls
