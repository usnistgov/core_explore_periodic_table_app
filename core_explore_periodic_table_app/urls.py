""" Url router for the Explore Period Table
"""

from django.conf.urls import url, include

import core_explore_periodic_table_app.views.user.views as user_views

urlpatterns = [
    url(r'^$', user_views.index, name='core_explore_periodic_table_index'),
]
