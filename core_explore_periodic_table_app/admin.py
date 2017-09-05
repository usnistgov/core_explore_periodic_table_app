"""
Url router for the administration site
"""
from django.conf.urls import url
from django.contrib import admin

from views.admin import views as admin_views

admin_urls = [
    url(r'^periodic_table$', admin_views.manage_periodic_table_index, name='manage_periodic_table_index'),
]

urls = admin.site.get_urls()
admin.site.get_urls = lambda: admin_urls + urls
