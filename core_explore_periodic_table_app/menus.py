""" Add Explore Period Table in main menu
"""

from django.urls import reverse
from menu import Menu, MenuItem

Menu.add_item(
    "explorer",
    MenuItem(
        "Query by Periodic Table", reverse("core_explore_periodic_table_index")
    ),
),

periodic_table_children = (
    MenuItem(
        "Settings",
        reverse("core-admin:manage_periodic_table_index"),
        icon="table",
    ),
)

Menu.add_item(
    "admin", MenuItem("PERIODIC TABLE", None, children=periodic_table_children)
)
