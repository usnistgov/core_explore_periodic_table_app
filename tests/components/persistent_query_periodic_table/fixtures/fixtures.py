""" Fixtures files for Persistent Query Periodic Table
"""

from core_main_app.utils.integration_tests.fixture_interface import FixtureInterface

from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)


class PersistentQueryPeriodicTableFixtures(FixtureInterface):
    """Persistent query periodic_table fixtures"""

    persistent_query_periodic_table_1 = None
    persistent_query_periodic_table_2 = None
    persistent_query_periodic_table_3 = None
    data_collection = None

    def insert_data(self):
        """Insert a set of Data.

        Returns:

        """
        # Make a connexion with a mock database
        self.generate_query_collection()

    def generate_query_collection(self):
        """Generate a PePersistentQueryPeriodicTable collection.

        Returns:

        """

        # NOTE: no xml_content to avoid using unsupported GridFS mock
        self.persistent_query_periodic_table_1 = PersistentQueryPeriodicTable(
            user_id="1", name="persistent_query_periodic_table_1"
        )

        self.persistent_query_periodic_table_1.save()

        self.persistent_query_periodic_table_2 = PersistentQueryPeriodicTable(
            user_id="2", name="persistent_query_periodic_table_2"
        )
        self.persistent_query_periodic_table_2.save()

        self.persistent_query_periodic_table_3 = PersistentQueryPeriodicTable(
            user_id="None", name="persistent_query_periodic_table_3"
        )
        self.persistent_query_periodic_table_3.save()

        self.data_collection = [
            self.persistent_query_periodic_table_1,
            self.persistent_query_periodic_table_2,
            self.persistent_query_periodic_table_3,
        ]
