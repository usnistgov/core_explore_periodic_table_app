"""
Url router for the administration site
"""
from django.contrib import admin
from django.urls import re_path

from core_explore_periodic_table_app.components.search_operator_mapping.models import (
    SearchOperatorMapping,
)
from core_explore_periodic_table_app.views.admin import views as admin_views
from core_main_app.admin import core_admin_site

admin_urls = [
    re_path(
        r"^periodic_table$",
        admin_views.manage_periodic_table_index,
        name="manage_periodic_table_index",
    ),
]

admin.site.register(SearchOperatorMapping)
urls = core_admin_site.get_urls()
core_admin_site.get_urls = lambda: admin_urls + urls
