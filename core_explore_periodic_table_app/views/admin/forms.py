""" Forms admin Periodic Table
"""
from django import forms

import core_composer_app.components.type_version_manager.api as type_version_manager_api


class AssociatedPeriodicTableTypeForm(forms.Form):
    """ Associated Periodic Table Type form
    """

    types_manager = forms.ChoiceField(label="", required=False)

    def __init__(self, *args, **kwargs):
        super(AssociatedPeriodicTableTypeForm, self).__init__(*args, **kwargs)
        self.fields["types_manager"].choices = _get_types_versions()


def _get_types_versions():
    """ Get types versions.

    Returns:
        List of types versions.

    """
    type_list = []
    try:
        # display all global types
        type_version_list = type_version_manager_api.get_active_global_version_manager()
        for type_item in type_version_list:
            type_list.append((type_item.id, type_item.title))
    except Exception:
        pass

    return type_list
