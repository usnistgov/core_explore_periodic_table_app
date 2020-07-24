"""Core Explore Period Table App Settings
"""
from django.conf import settings

if not settings.configured:
    settings.configure()

PERIODIC_TABLE_SEARCH_OPERATOR = getattr(
    settings, "PERIODIC_TABLE_SEARCH_OPERATOR", "periodic_table"
)
""" :py:class:`string`: name of the field which notice that 
     a search operator is compatible with the periodic table type path.
"""
