""" Url router for the explore periodic table application
"""

from django.conf.urls import include
from django.urls import re_path

from core_main_app.admin import core_admin_site

urlpatterns = [
    re_path(r"^core-admin/", core_admin_site.urls),
    re_path(r"^", include("core_main_app.urls")),
    re_path(r"^", include("core_explore_periodic_table_app.urls")),
]
