""" Url router for the Explore Period Table
"""

from django.conf.urls import include
from django.conf.urls import re_path

from core_explore_periodic_table_app.views.user import (
    views as user_views,
    ajax as user_ajax,
)

urlpatterns = [
    re_path(r"^rest/", include("core_explore_periodic_table_app.rest.urls")),
    re_path(
        r"^$",
        user_views.PeriodicTableBuildQueryView.as_view(),
        name="core_explore_periodic_table_index",
    ),
    re_path(
        r"^(?P<query_id>\w+)$",
        user_views.PeriodicTableBuildQueryView.as_view(),
        name="core_explore_periodic_table_index",
    ),
    re_path(
        r"^results-redirect",
        user_views.ResultQueryRedirectPeriodicSearchView.as_view(),
        name="core_explore_periodic_table_redirect",
    ),
    re_path(
        r"^get-persistent-query-url$",
        user_ajax.CreatePersistentQueryUrlPeriodicTableView.as_view(),
        name="core_explore_periodic_table_get_persistent_query_url",
    ),
]
