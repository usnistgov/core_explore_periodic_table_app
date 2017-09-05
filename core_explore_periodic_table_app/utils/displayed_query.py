"""Util to build user readable queries
"""
from core_explore_example_app.utils.displayed_query import build_pretty_criteria, build_and_pretty_criteria


def fields_to_pretty_query(values, path):
    """Transforms fields from the HTML form into pretty representation

    Args:
        values:
        path:

    Returns:

    """
    query = ""
    # build the query
    for value in values:
        criteria = build_pretty_criteria(path, "is", value, False)
        if values.index(value) == 0:
            query += criteria
        else:
            query = build_and_pretty_criteria(query, criteria)
    return query
