"""Url router for the REST API
"""
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

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
]

urlpatterns = format_suffix_patterns(urlpatterns)
