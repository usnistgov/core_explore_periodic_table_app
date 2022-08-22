""" Forms admin Periodic Table
"""
from django import forms

from core_explore_keyword_app.components.search_operator import (
    api as search_operator_api,
)
from core_explore_periodic_table_app.components.search_operator_mapping import (
    api as search_operator_mapping_api,
)


def _initial_form():
    """Set the initial state of the form.

    Returns:
        List of fields select.

    """
    search_operator_mapping = search_operator_mapping_api.get_all()
    result = []

    for mapping in search_operator_mapping:
        result.append(str(mapping.search_operator.id))

    return result


def _get_search_operators():
    """Get types versions.

    Returns:
        List of types versions.

    """
    type_list = []
    try:
        # display all global types
        all_search_operator_list = search_operator_api.get_all()
        for search_operator in all_search_operator_list:
            type_list.append((search_operator.id, search_operator.name))
    except Exception:
        pass

    return type_list


class AssociatedPeriodicTableSearchOperatorForm(forms.Form):
    """Associated Periodic Table Type form"""

    search_operator_list = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Search operator list",
        error_messages="",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["search_operator_list"].initial = _initial_form()
        self.fields["search_operator_list"].choices = _get_search_operators()
