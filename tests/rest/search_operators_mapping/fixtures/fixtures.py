""" Fixtures files for Data
"""

from core_main_app.utils.integration_tests.fixture_interface import (
    FixtureInterface,
)
from core_explore_keyword_app.components.search_operator.models import (
    SearchOperator,
)
from core_explore_periodic_table_app.components.search_operator_mapping.models import (
    SearchOperatorMapping,
)
from core_explore_periodic_table_app.rest.search_operator_mapping.serializers import (
    SearchOperatorMappingSerializer,
)


class SearchOperatorMappingFixtures(FixtureInterface):
    """Search Operator Mapping fixture"""

    search_operator_mapping_1 = None
    search_operator_mapping_2 = None
    search_operator_mapping_3 = None

    search_operator_mapping_1_serialized = None
    search_operator_mapping_2_serialized = None
    search_operator_mapping_3_serialized = None

    search_operator_1 = None
    search_operator_2 = None
    search_operator_3 = None

    def insert_data(self):
        """Insert a set of Search Operator Mapping.

        Returns:

        """
        # Make a connexion with a mock database
        self.generate_search_operator_collection()
        self.generate_search_operator_mapping_collection()

    def generate_search_operator_collection(self):
        """Generate a Search Operator collection.

        Returns:

        """
        self.search_operator_1 = SearchOperator(
            name="name1", xpath_list=["a/b/c"], dot_notation_list=["a.b.c"]
        )
        self.search_operator_1.save()

        self.search_operator_2 = SearchOperator(
            name="name2", xpath_list=["d/e/f"], dot_notation_list=["d.e.f"]
        )
        self.search_operator_2.save()

        self.search_operator_3 = SearchOperator(
            name="name3", xpath_list=["g/h/i"], dot_notation_list=["g.h.i"]
        )
        self.search_operator_3.save()

        self.search_operator_collection = [
            self.search_operator_1,
            self.search_operator_2,
            self.search_operator_3,
        ]

    def generate_search_operator_mapping_collection(self):
        """Generate a Search Operator Mapping collection.

        Returns:

        """
        self.search_operator_mapping_1 = SearchOperatorMapping(
            search_operator=self.search_operator_1
        )
        self.search_operator_mapping_1.save()

        self.search_operator_mapping_2 = SearchOperatorMapping(
            search_operator=self.search_operator_2
        )
        self.search_operator_mapping_2.save()

        serializer = SearchOperatorMappingSerializer(
            data=[
                self.search_operator_mapping_1,
                self.search_operator_mapping_2,
            ],
            many=True,
        )

        serializer.is_valid()

        self.search_operator_mapping_collection = serializer.data

        self.search_operator_mapping_1_serialized = (
            self.search_operator_mapping_collection[0]
        )
        self.search_operator_mapping_2_serialized = (
            self.search_operator_mapping_collection[1]
        )
