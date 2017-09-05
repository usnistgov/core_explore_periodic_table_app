""" Url router for the Explore Period Table
"""

from django.conf.urls import url

import core_explore_periodic_table_app.views.user.ajax as user_ajax
from core_explore_example_app.views.user import views as explore_example_app_user_views
from core_explore_periodic_table_app.utils.mongo_query import fields_to_query
from core_explore_periodic_table_app.views.user.views import PeriodicTableBuildQueryView

urlpatterns = [
    url(r'^$', PeriodicTableBuildQueryView.as_view(), name='core_explore_periodic_table_index'),
    url(r'^(?P<template_id>\w+)$',
        PeriodicTableBuildQueryView.as_view(),
        name='core_explore_periodic_table_index'),
    url(r'^(?P<template_id>\w+)/(?P<query_id>\w+)$',
        PeriodicTableBuildQueryView.as_view(),
        name='core_explore_periodic_table_index'),

    url(r'^save-query$', user_ajax.PeriodicTableSaveQueryView.as_view(fields_to_query_func=fields_to_query),
        name='core_explore_periodic_table_save_query'),

    url(r'^results/(?P<template_id>\w+)/(?P<query_id>\w+)$',
        explore_example_app_user_views.ResultQueryView.as_view(
            back_to_query_redirect='core_explore_periodic_table_index'),
        name='core_explore_periodic_table_results'),

    url(r'^get-query-values$', user_ajax.get_query_values, name='core_explore_periodic_table_get_query_values'),
    url(r'^submit-query$', user_ajax.submit_query, name='core_explore_periodic_table_submit_query'),
]
