""" Periodic table's views
"""
from core_main_app.utils.rendering import render


def index(request):
    """ Periodic table Index

    Args:
        request:

    Returns:

    """

    context = {
    }

    assets = {
    }

    return render(request, 'core_explore_periodic_table_app/user/index.html', context=context, assets=assets)
