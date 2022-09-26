"""Explore periodic table app Ajax views
"""

from core_explore_common_app.views.user.ajax import (
    CreatePersistentQueryUrlView,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)


class CreatePersistentQueryUrlPeriodicTableView(CreatePersistentQueryUrlView):
    """Create the persistent url from a Query"""

    view_to_reverse = "core_explore_periodic_table_redirect"

    @staticmethod
    def _create_persistent_query(query):
        # create the persistent query
        return PersistentQueryPeriodicTable(
            user_id=query.user_id,
            content=query.content,
            data_sources=query.data_sources,
        )
