core_explore_periodic_table_app
===============================

core_explore_periodic_table_app is a Django app.

Quick start
===========

1. Add "core_explore_periodic_table_app" to your INSTALLED_APPS setting
-----------------------------------------------------------------------

.. code:: python

    INSTALLED_APPS = [
      ...
      'core_explore_periodic_table_app',
    ]

2. Include the core_explore_periodic_table_app URLconf in your project urls.py
------------------------------------------------------------------------------

.. code:: python

      url(r'^explore/periodic_table/', include("core_explore_periodic_table_app.urls")),
