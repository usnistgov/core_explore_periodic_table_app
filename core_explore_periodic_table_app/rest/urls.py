"""Url router for the REST API
"""
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from core_explore_periodic_table_app.rest.persistent_query_periodic_table import (
    views as persistent_query_periodic_table_views,
)
from core_explore_periodic_table_app.rest.search_operator_mapping import (
    views as search_operators_mapping_views,
)

urlpatterns = [
    re_path(
        r"^search_operators_mapping/$",
        search_operators_mapping_views.SearchOperatorsMapping.as_view(),
        name="core_explore_periodic_table_app_rest_search_operators_mapping",
    ),
    re_path(
        r"^search_operators_mapping/(?P<pk>\w+)/$",
        search_operators_mapping_views.SearchOperatorMappingDetail.as_view(),
        name="core_explore_periodic_table_app_rest_search_operators_mapping_detail",
    ),
    re_path(
        r"^admin/persistent_query_periodic_table/$",
        persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
        name="core_explore_periodic_table_app_rest_persistent_query_periodic_table_admin_list",
    ),
    re_path(
        r"^persistent_query_periodic_table/$",
        persistent_query_periodic_table_views.PersistentQueryPeriodicTableList.as_view(),
        name="core_explore_periodic_table_app_rest_persistent_query_periodic_table_list",
    ),
    re_path(
        r"^persistent_query_periodic_table/(?P<pk>\w+)/$",
        persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
        name="core_explore_periodic_table_app_rest_persistent_query_periodic_table_detail",
    ),
    re_path(
        r"^persistent_query_periodic_table/name/(?P<name>\w+)/$",
        persistent_query_periodic_table_views.PersistentQueryPeriodicTableByName.as_view(),
        name="core_explore_periodic_table_app_rest_persistent_query_periodic_table_name",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
