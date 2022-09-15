""" Integration Test Persistent Query Periodic Table
"""
from core_main_app.utils.integration_tests.integration_base_test_case import (
    MongoIntegrationBaseTestCase,
)
from core_main_app.utils.tests_tools.MockUser import create_mock_user
from core_main_app.utils.tests_tools.RequestMock import RequestMock

from core_explore_periodic_table_app.rest.search_operator_mapping import (
    views as search_operator_mapping_views,
)
from tests.rest.search_operators_mapping.fixtures.fixtures import (
    SearchOperatorMappingFixtures,
)

fixture_search_operator_mapping = SearchOperatorMappingFixtures()


class TestSearchOperatorMapping(MongoIntegrationBaseTestCase):
    """Test Search Operator Mapping"""

    fixture = fixture_search_operator_mapping

    def test_get_all_search_operator_mapping_return_collection(self):
        """test_get_all_search_operator_mapping_return_collection"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
        )

        # Assert
        self.assertListEqual(
            response.data, self.fixture.search_operator_mapping_collection
        )

    def test_get_search_operator_mapping_return_object(self):
        """test_get_search_operator_mapping_return_object"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(
            response.data, self.fixture.search_operator_mapping_1_serialized
        )

    def test_get_search_operator_mapping_with_wrong_param(self):
        """test_get_search_operator_mapping_with_wrong_param"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": "123456789012345678901234"},
        )

        # Assert
        self.assertEqual(response.status_code, 500)

    def test_add_search_operator_mapping(self):
        """test_add_search_operator_mapping"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_post(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
            data={"search_operator": str(self.fixture.search_operator_1.id)},
        )

        # Assert
        self.assertEqual(
            response.data["search_operator"], self.fixture.search_operator_1.id
        )

    def test_add_wrong_search_operator_mapping(self):
        """test_add_wrong_search_operator_mapping"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_post(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
            data={"search_operator": -1},
        )

        # Assert
        self.assertEqual(response.status_code, 400)

    def test_update_search_operator_mapping(self):
        """test_update_search_operator_mapping"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_patch(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
            data={"search_operator": str(self.fixture.search_operator_3.id)},
        )

        # Assert
        self.assertEqual(
            response.data["search_operator"], self.fixture.search_operator_3.id
        )

    def test_delete_search_operator_mapping(self):
        """test_delete_search_operator_mapping"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_delete(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(response.status_code, 204)
