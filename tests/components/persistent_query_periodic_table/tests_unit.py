""" Unit tests for PersistentQueryPeriodicTable.
"""
from unittest import TestCase, mock

from mock import patch

from core_main_app.access_control.exceptions import AccessControlError
from core_main_app.commons import exceptions
from core_main_app.utils.tests_tools.MockUser import create_mock_user
from core_explore_periodic_table_app.components.persistent_query_periodic_table import (
    api as persistent_query_periodic_table_api,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)


class TestPersistentQueryPeriodicTableGetById(TestCase):
    """Test Persistent Query Periodic Table Get By Id"""

    @patch.object(PersistentQueryPeriodicTable, "get_by_id")
    def test_persistent_query_periodic_table_get_by_id_return_data_if_found(
        self, mock_get_by_id
    ):
        """test_persistent_query_periodic_table_get_by_id_return_data_if_found"""

        # Arrange
        expected_result = PersistentQueryPeriodicTable(user_id="1")
        mock_get_by_id.return_value = expected_result
        mock_user = create_mock_user("1")

        # Act # Assert
        self.assertEqual(
            persistent_query_periodic_table_api.get_by_id("mock_id", mock_user),
            expected_result,
        )

    def test_persistent_query_periodic_table_get_by_id_raises_model_error_if_not_found(
        self,
    ):
        """test_persistent_query_periodic_table_get_by_id_raises_model_error_if_not_found"""

        # Arrange
        mock_user = create_mock_user("1")

        # Act # Assert
        with self.assertRaises(exceptions.ModelError):
            persistent_query_periodic_table_api.get_by_id("mock_id", mock_user)

    @patch.object(PersistentQueryPeriodicTable, "get_by_id")
    def test_persistent_query_periodic_table_get_by_id_raises_does_not_exist_error_if_not_found(
        self, mock_get_by_id
    ):
        """test_persistent_query_periodic_table_get_by_id_raises_does_not_exist_error_if_not_found"""

        # Arrange
        mock_get_by_id.side_effect = exceptions.DoesNotExist(message="mock error")
        mock_user = create_mock_user("1")

        # Act # Assert
        with self.assertRaises(exceptions.DoesNotExist):
            persistent_query_periodic_table_api.get_by_id("mock_id", mock_user)


class TestsPersistentQueryPeriodicTableGetByName(TestCase):
    """Tests Persistent Query Periodic Table Get By Name"""

    @mock.patch.object(PersistentQueryPeriodicTable, "get_by_name")
    def test_persistent_query_periodic_table_get_by_name_return_data_if_found(
        self, mock_get_by_name
    ):
        """test_persistent_query_periodic_table_get_by_name_return_data_if_found"""

        # Arrange
        expected_result = PersistentQueryPeriodicTable(user_id="1")
        mock_get_by_name.return_value = expected_result
        mock_user = create_mock_user("1")

        # Act # Assert
        self.assertEqual(
            persistent_query_periodic_table_api.get_by_name("mock_name", mock_user),
            expected_result,
        )

    @patch.object(PersistentQueryPeriodicTable, "get_by_name")
    def test_persistent_query_periodic_table_get_by_name_raises_error_if_not_found(
        self, mock_get_by_name
    ):
        """test_persistent_query_periodic_table_get_by_name_raises_error_if_not_found"""

        # Arrange
        mock_get_by_name.side_effect = exceptions.DoesNotExist(message="mock error")
        mock_user = create_mock_user("1")

        # Act # Assert
        with self.assertRaises(exceptions.DoesNotExist):
            persistent_query_periodic_table_api.get_by_name("mock_id", mock_user)


class TestsPersistentQueryPeriodicTableUpsert(TestCase):
    """Test Persistent Query Periodic Table Upsert"""

    def setUp(self) -> None:
        self.mock_persistent_query_periodic_table = PersistentQueryPeriodicTable(
            user_id="1",
            name="mock_periodic_table",
            content={"content_test"},
            data_sources=[],
        )

    @patch.object(PersistentQueryPeriodicTable, "save")
    def test_persistent_query_periodic_table_upsert_return_data(self, mock_save):
        """test_persistent_query_periodic_table_upsert_return_data"""

        # Arrange
        mock_save.return_value = self.mock_persistent_query_periodic_table
        mock_user = create_mock_user("1")

        # Act
        result = persistent_query_periodic_table_api.upsert(
            self.mock_persistent_query_periodic_table, mock_user
        )

        # Assert
        self.assertIsInstance(result, PersistentQueryPeriodicTable)


class TestsPersistentQueryPeriodicTableDelete(TestCase):
    """Test Persistent Query Periodic Table Delete"""

    @patch.object(PersistentQueryPeriodicTable, "delete")
    def test_returns_no_error(self, mock_delete):
        """test_returns_no_error"""

        # Arrange
        mock_delete.return_value = None
        mock_user = create_mock_user("1")

        # Act
        persistent_query_periodic_table_api.delete(
            PersistentQueryPeriodicTable(user_id="1"), mock_user
        )


class TestsPersistentQueryPeriodicTableGetAll(TestCase):
    """Test Persistent Query Periodic Table Get All"""

    @patch.object(PersistentQueryPeriodicTable, "get_all")
    def test_returns_no_error(self, mock_get_all):
        """test_returns_no_error"""

        # Arrange
        expected_result = {
            PersistentQueryPeriodicTable(id=1, user_id="1"),
            PersistentQueryPeriodicTable(id=2, user_id="1"),
        }
        mock_get_all.return_value = expected_result

        mock_user = create_mock_user("1", is_superuser=True, is_staff=True)

        # Act # Assert
        self.assertEqual(
            persistent_query_periodic_table_api.get_all(mock_user), expected_result
        )

    @patch.object(PersistentQueryPeriodicTable, "get_all")
    def test_persistent_query_periodic_table_get_all_raises_error_if_not_admin(
        self, mock_get_all
    ):
        """test_persistent_query_periodic_table_get_all_raises_error_if_not_admin"""

        # Arrange
        mock_get_all.side_effect = AccessControlError
        mock_user = create_mock_user("1")

        # Act # Assert
        with self.assertRaises(AccessControlError):
            persistent_query_periodic_table_api.get_all(mock_user)


class TestsPersistentQueryPeriodicTableGetAllByUser(TestCase):
    """Test Persistent Query Periodic Table Get All By User"""

    @patch.object(PersistentQueryPeriodicTable, "get_all_by_user")
    def test_returns_no_error(self, mock_get_all_by_user):
        """test_returns_no_error"""

        # Arrange
        expected_result = {
            PersistentQueryPeriodicTable(id=1, user_id="1"),
            PersistentQueryPeriodicTable(id=2, user_id="1"),
        }
        mock_get_all_by_user.return_value = expected_result

        mock_user = create_mock_user("1")

        # Act # Assert
        self.assertEqual(
            persistent_query_periodic_table_api.get_all_by_user(mock_user),
            expected_result,
        )
