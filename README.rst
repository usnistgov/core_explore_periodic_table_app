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

    re_path(r'^explore/periodic_table/', include("core_explore_periodic_table_app.urls")),

3. Configure the Search Operators
---------------------------------

Configure the Search by periodic table app by adding search operators pointing to chemical elements in the CDCS data.
Start by adding a search operator:

.. code:: python

    import requests

    payload = {
        "name": "chemical",
        "xpath_list": [
            "/experiment/experimentType/tracerDiffusivity/diffusingSpecies/element",
            "/experiment/experimentType/tracerDiffusivity/material/Composition/constituents/constituent/element"
        ]
    }

    requests.post(
        SERVER_URI + "/explore/keyword/rest/search_operators/", data=payload, auth=(USER, PASSWORD)
    )

Then, tell the periodic table app to use one or many search operators by adding mappings:

.. code:: python

    import requests

    payload = {
        "search_operator": "5f49048f3b3689f92cb84f41"
    }

    requests.post(
        SERVER_URI + "/explore/periodic_table/rest/search_operators_mapping/", data=payload, auth=(USER, PASSWORD)
    )
