""" Permission Tests for Persistent Query Periodic Table
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


class TestSearchOperatorMappingPermissions(MongoIntegrationBaseTestCase):
    """Test Search Operator Mapping Permissions"""

    fixture = fixture_search_operator_mapping

    def test_get_all_staff_return_200(self):
        """test_get_all_staff_return_200"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
        )

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_get_all_anonymous_return_403(self):
        """test_get_all_anonymous_return_403"""

        # Arrange
        user = create_mock_user("1", is_anonymous=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_get_all_superuser_return_403(self):
        """test_get_all_superuser_return_403"""

        # Arrange
        user = create_mock_user("1", is_superuser=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_get_all_authenticated_return_403(self):
        """test_get_all_authenticated_return_403"""

        # Arrange
        user = create_mock_user("1")

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_get_search_operator_mapping_staff_return_200(self):
        """test_get_search_operator_mapping_staff_return_200"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_get_search_operator_mapping_anonymous_return_403(self):
        """test_get_search_operator_mapping_anonymous_return_403"""

        # Arrange
        user = create_mock_user("1", is_anonymous=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_get_search_operator_mapping_superuser_return_403(self):
        """test_get_search_operator_mapping_superuser_return_403"""

        # Arrange
        user = create_mock_user("1", is_superuser=True)

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_get_search_operator_mapping_authenticated_return_403(self):
        """test_get_search_operator_mapping_authenticated_return_403"""

        # Arrange
        user = create_mock_user("1")

        # Act
        response = RequestMock.do_request_get(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_add_search_operator_mapping_staff_return_201(self):
        """test_add_search_operator_mapping_staff_return_201"""

        # Arrange
        user = create_mock_user("1", is_staff=True)

        # Act
        response = RequestMock.do_request_post(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
            data={"search_operator": str(self.fixture.search_operator_3.id)},
        )

        # Assert
        self.assertEqual(response.status_code, 201)

    def test_add_search_operator_mapping_anonymous_return_403(self):
        """test_add_search_operator_mapping_anonymous_return_403"""

        # Arrange
        user = create_mock_user("1", is_anonymous=True)

        # Act
        response = RequestMock.do_request_post(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
            data={"search_operator": str(self.fixture.search_operator_1.id)},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_add_search_operator_mapping_superuser_return_403(self):
        """test_add_search_operator_mapping_superuser_return_403"""

        # Arrange
        user = create_mock_user("1", is_superuser=True)

        # Act
        response = RequestMock.do_request_post(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
            data={"search_operator": str(self.fixture.search_operator_1.id)},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_add_search_operator_mapping_authenticated_return_403(self):
        """test_add_search_operator_mapping_authenticated_return_403"""

        # Arrange
        user = create_mock_user("1")

        # Act
        response = RequestMock.do_request_post(
            search_operator_mapping_views.SearchOperatorsMapping.as_view(),
            user,
            data={"search_operator": str(self.fixture.search_operator_1.id)},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_update_search_operator_mapping_staff_return_200(self):
        """test_update_search_operator_mapping_staff_return_200"""

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
        self.assertEqual(response.status_code, 200)

    def test_update_search_operator_mapping_anonymous_return_403(self):
        """test_update_search_operator_mapping_anonymous_return_403"""

        # Arrange
        user = create_mock_user("1", is_anonymous=True)

        # Act
        response = RequestMock.do_request_patch(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
            data={"search_operator": str(self.fixture.search_operator_2.id)},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_update_search_operator_mapping_superuser_return_403(self):
        """test_update_search_operator_mapping_superuser_return_403"""

        # Arrange
        user = create_mock_user("1", is_superuser=True)

        # Act
        response = RequestMock.do_request_patch(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
            data={"search_operator": str(self.fixture.search_operator_2.id)},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_update_search_operator_mapping_authenticated_return_403(self):
        """test_update_search_operator_mapping_authenticated_return_403"""

        # Arrange
        user = create_mock_user("1")

        # Act
        response = RequestMock.do_request_patch(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
            data={"search_operator": str(self.fixture.search_operator_2.id)},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_delete_search_operator_mapping_staff_return_204(self):
        """test_delete_search_operator_mapping_staff_return_204"""

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

    def test_delete_search_operator_mapping_anonymous_return_403(self):
        """test_delete_search_operator_mapping_anonymous_return_403"""

        # Arrange
        user = create_mock_user("1", is_anonymous=True)

        # Act
        response = RequestMock.do_request_delete(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_delete_search_operator_mapping_superuser_return_403(self):
        """test_delete_search_operator_mapping_superuser_return_403"""

        # Arrange
        user = create_mock_user("1", is_superuser=True)

        # Act
        response = RequestMock.do_request_delete(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(response.status_code, 403)

    def test_delete_search_operator_mapping_authenticated_return_403(self):
        """test_delete_search_operator_mapping_authenticated_return_403"""

        # Arrange
        user = create_mock_user("1")

        # Act
        response = RequestMock.do_request_delete(
            search_operator_mapping_views.SearchOperatorMappingDetail.as_view(),
            user,
            param={"pk": self.fixture.search_operator_mapping_1.id},
        )

        # Assert
        self.assertEqual(response.status_code, 403)
