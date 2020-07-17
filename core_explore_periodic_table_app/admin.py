"""
Url router for the administration site
"""
from django.urls import re_path
from django.contrib import admin
from core_explore_periodic_table_app.views.admin import views as admin_views

admin_urls = [
    re_path(
        r"^periodic_table$",
        admin_views.manage_periodic_table_index,
        name="manage_periodic_table_index",
    ),
]

urls = admin.site.get_urls()
admin.site.get_urls = lambda: admin_urls + urls
