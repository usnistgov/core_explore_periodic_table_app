""" Add Explore Period Table in main menu
"""

from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

# FIXME: CHECK AUTHENTICATION !
Menu.add_item(
    "main", MenuItem("Query by Periodic Table", reverse("core_explore_periodic_table_index"))
)
