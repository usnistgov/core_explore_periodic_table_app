""" Unit Test Persistent Query Periodic Table
"""

from django.contrib.auth.models import AnonymousUser

from core_main_app.access_control.exceptions import AccessControlError
from core_main_app.utils.integration_tests.integration_base_test_case import (
    IntegrationBaseTestCase,
)
from core_main_app.utils.tests_tools.MockUser import create_mock_user

from core_explore_common_app.settings import (
    CAN_ANONYMOUS_ACCESS_PUBLIC_DOCUMENT,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table import (
    api as persistent_query_periodic_table_api,
)
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)
from tests.components.persistent_query_periodic_table.fixtures.fixtures import (
    PersistentQueryPeriodicTableFixtures,
)

fixture_persistent_query_periodic_table = (
    PersistentQueryPeriodicTableFixtures()
)


class TestPersistentQueryPeriodicTableGetById(IntegrationBaseTestCase):
    """Test Persistent Query Periodic Table Get By Id"""

    fixture = fixture_persistent_query_periodic_table

    def test_get_by_id_as_superuser_returns_persistent_query_periodic_table(
        self,
    ):
        """test_get_by_id_as_superuser_returns_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table_id = (
            self.fixture.persistent_query_periodic_table_1.id
        )
        mock_user = create_mock_user("0", is_staff=True, is_superuser=True)

        # Act
        persistent_query_periodic_table = (
            persistent_query_periodic_table_api.get_by_id(
                persistent_query_periodic_table_id, mock_user
            )
        )

        # Assert
        self.assertTrue(
            isinstance(
                persistent_query_periodic_table, PersistentQueryPeriodicTable
            )
        )

    def test_get_by_id_as_owner_returns_persistent_query_periodic_table(self):
        """test_get_by_id_as_owner_returns_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table_id = (
            self.fixture.persistent_query_periodic_table_1.id
        )
        mock_user = create_mock_user("1")

        # Act
        persistent_query_periodic_table = (
            persistent_query_periodic_table_api.get_by_id(
                persistent_query_periodic_table_id, mock_user
            )
        )

        # Assert
        self.assertTrue(
            isinstance(
                persistent_query_periodic_table, PersistentQueryPeriodicTable
            )
        )

    def test_get_by_id_as_anonymous_user(self):
        """test_get_by_id_as_anonymous_user"""

        # Arrange
        persistent_query_periodic_table_id = (
            self.fixture.persistent_query_periodic_table_1.id
        )

        # Act # Assert
        if CAN_ANONYMOUS_ACCESS_PUBLIC_DOCUMENT:
            self.assertTrue(
                isinstance(
                    persistent_query_periodic_table_api.get_by_id(
                        persistent_query_periodic_table_id, AnonymousUser()
                    ),
                    PersistentQueryPeriodicTable,
                )
            )

        else:
            with self.assertRaises(AccessControlError):
                persistent_query_periodic_table_api.get_by_id(
                    persistent_query_periodic_table_id, AnonymousUser()
                )

    def test_get_by_id_as_user_not_owner(self):
        """test_get_by_id_as_user_not_owner"""

        # Arrange
        persistent_query_periodic_table_id = (
            self.fixture.persistent_query_periodic_table_1.id
        )
        mock_user = create_mock_user("0")

        # Act # Assert

        self.assertTrue(
            isinstance(
                persistent_query_periodic_table_api.get_by_id(
                    persistent_query_periodic_table_id, mock_user
                ),
                PersistentQueryPeriodicTable,
            )
        )


class TestPersistentQueryPeriodicTableGetByName(IntegrationBaseTestCase):
    """Test Persistent Query Periodic Table Get By Name"""

    fixture = fixture_persistent_query_periodic_table

    def test_get_by_name_as_superuser_returns_persistent_query_periodic_table(
        self,
    ):
        """test_get_by_name_as_superuser_returns_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table_name = (
            self.fixture.persistent_query_periodic_table_1.name
        )
        mock_user = create_mock_user("0", is_staff=True, is_superuser=True)

        # Act
        persistent_query_periodic_table = (
            persistent_query_periodic_table_api.get_by_name(
                persistent_query_periodic_table_name, mock_user
            )
        )

        # Assert
        self.assertTrue(
            isinstance(
                persistent_query_periodic_table, PersistentQueryPeriodicTable
            )
        )

    def test_get_by_name_as_owner_returns_persistent_query_periodic_table(
        self,
    ):
        """test_get_by_name_as_owner_returns_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table_name = (
            self.fixture.persistent_query_periodic_table_1.name
        )
        mock_user = create_mock_user("1")

        # Act
        persistent_query_periodic_table = (
            persistent_query_periodic_table_api.get_by_name(
                persistent_query_periodic_table_name, mock_user
            )
        )

        # Assert
        self.assertTrue(
            isinstance(
                persistent_query_periodic_table, PersistentQueryPeriodicTable
            )
        )

    def test_get_by_name_as_user_not_owner(self):
        """test_get_by_name_as_user_not_owner"""

        # Arrange
        persistent_query_periodic_table_name = (
            self.fixture.persistent_query_periodic_table_1.name
        )
        mock_user = create_mock_user("0")

        # Act # Assert
        self.assertTrue(
            isinstance(
                persistent_query_periodic_table_api.get_by_name(
                    persistent_query_periodic_table_name, mock_user
                ),
                PersistentQueryPeriodicTable,
            )
        )

    def test_get_by_name_as_anonymous_user(self):
        """test_get_by_name_as_anonymous_user"""

        # Arrange
        persistent_query_periodic_table_name = (
            self.fixture.persistent_query_periodic_table_1.name
        )

        # Act # Assert
        if CAN_ANONYMOUS_ACCESS_PUBLIC_DOCUMENT:
            self.assertTrue(
                isinstance(
                    persistent_query_periodic_table_api.get_by_name(
                        persistent_query_periodic_table_name, AnonymousUser()
                    ),
                    PersistentQueryPeriodicTable,
                )
            )

        else:
            with self.assertRaises(AccessControlError):
                persistent_query_periodic_table_api.get_by_name(
                    persistent_query_periodic_table_name, AnonymousUser()
                )


class TestPersistentQueryPeriodicTableDelete(IntegrationBaseTestCase):
    """Test Persistent Query Periodic Table Delete"""

    fixture = fixture_persistent_query_periodic_table

    def test_delete_others_as_superuser_deletes_persistent_query_periodic_table(
        self,
    ):
        """test_delete_others_as_superuser_deletes_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table = (
            self.fixture.persistent_query_periodic_table_1
        )
        mock_user = create_mock_user("0", is_staff=True, is_superuser=True)

        # Act
        persistent_query_periodic_table_api.delete(
            persistent_query_periodic_table, mock_user
        )

    def test_delete_own_table_deletes_persistent_query_periodic_table(
        self,
    ):
        """test_delete_own_table_deletes_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table = (
            self.fixture.persistent_query_periodic_table_1
        )
        mock_user = create_mock_user("1")

        # Act
        persistent_query_periodic_table_api.delete(
            persistent_query_periodic_table, mock_user
        )

    def test_delete_others_as_user_raises_error(self):
        """test_delete_others_as_user_raises_error"""

        # Arrange
        persistent_query_periodic_table = (
            self.fixture.persistent_query_periodic_table_1
        )
        mock_user = create_mock_user("0")

        # Act # Assert
        with self.assertRaises(AccessControlError):
            persistent_query_periodic_table_api.delete(
                persistent_query_periodic_table, mock_user
            )

    def test_delete_others_as_anonymous_raises_error(
        self,
    ):
        """test_delete_others_as_anonymous_raises_error"""

        # Arrange
        persistent_query_periodic_table = (
            self.fixture.persistent_query_periodic_table_1
        )

        # Act # Assert
        with self.assertRaises(AccessControlError):
            persistent_query_periodic_table_api.delete(
                persistent_query_periodic_table, AnonymousUser()
            )


class TestPersistentQueryPeriodicTableUpdate(IntegrationBaseTestCase):
    """Test Persistent Query Periodic Table Update"""

    fixture = fixture_persistent_query_periodic_table

    def test_update_others_as_superuser_updates_persistent_query_periodic_table(
        self,
    ):
        """test_update_others_as_superuser_updates_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table = (
            self.fixture.persistent_query_periodic_table_1
        )
        persistent_query_periodic_table.name = (
            "new_name_persistent_query_periodic_table_1"
        )
        mock_user = create_mock_user("0", is_staff=True, is_superuser=True)
        # Act
        result = persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, mock_user
        )
        # Assert
        self.assertTrue(isinstance(result, PersistentQueryPeriodicTable))
        self.assertTrue(
            result.name, "new_name_persistent_query_periodic_table_1"
        )

    def test_update_own_updates_persistent_query_periodic_table(
        self,
    ):
        """test_update_own_updates_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table = (
            self.fixture.persistent_query_periodic_table_1
        )
        mock_user = create_mock_user("1")
        persistent_query_periodic_table.name = (
            "new_name_persistent_query_periodic_table_1"
        )
        # Act
        result = persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, mock_user
        )
        # Assert
        self.assertTrue(isinstance(result, PersistentQueryPeriodicTable))
        self.assertTrue(
            result.name, "new_name_persistent_query_periodic_table_1"
        )

    def test_update_others_as_user_raises_error(self):
        """test_update_others_as_user_raises_error"""

        # Arrange
        persistent_query_periodic_table = (
            self.fixture.persistent_query_periodic_table_1
        )
        persistent_query_periodic_table.name = (
            "new_name_persistent_query_periodic_table_1"
        )
        mock_user = create_mock_user("0")

        # Act # Assert
        with self.assertRaises(AccessControlError):
            persistent_query_periodic_table_api.upsert(
                persistent_query_periodic_table, mock_user
            )

    def test_update_others_as_anonymous_raises_error(
        self,
    ):
        """test_update_others_as_anonymous_raises_error"""

        # Arrange
        persistent_query_periodic_table = (
            self.fixture.persistent_query_periodic_table_1
        )

        # Act # Assert
        with self.assertRaises(AccessControlError):
            persistent_query_periodic_table_api.upsert(
                persistent_query_periodic_table, AnonymousUser()
            )


class TestPersistentQueryPeriodicTableCreate(IntegrationBaseTestCase):
    """Test Persistent Query Periodic Table Create"""

    fixture = fixture_persistent_query_periodic_table

    def test_create_for_others_as_superuser_creates_persistent_query_periodic_table(
        self,
    ):
        """test_create_for_others_as_superuser_creates_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table = PersistentQueryPeriodicTable(
            name="new_persistent_query_periodic_table", user_id="0"
        )
        mock_user = create_mock_user("0", is_staff=True, is_superuser=True)
        # Act
        result = persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, mock_user
        )
        # Assert
        self.assertTrue(isinstance(result, PersistentQueryPeriodicTable))
        self.assertTrue(result.name, "new_persistent_query_periodic_table")

    def test_create_as_user_creates_persistent_query_periodic_table(
        self,
    ):
        """test_create_as_user_creates_persistent_query_periodic_table"""

        # Arrange
        persistent_query_periodic_table = PersistentQueryPeriodicTable(
            name="new_persistent_query_periodic_table", user_id="1"
        )
        mock_user = create_mock_user("1")

        # Act
        result = persistent_query_periodic_table_api.upsert(
            persistent_query_periodic_table, mock_user
        )
        # Assert
        self.assertTrue(isinstance(result, PersistentQueryPeriodicTable))
        self.assertTrue(result.name, "new_persistent_query_periodic_table")

    def test_create_as_anonymous_user(self):
        """test_create_as_anonymous_user"""

        # Arrange
        persistent_query_periodic_table = PersistentQueryPeriodicTable(
            name="new_persistent_query_periodic_table", user_id="None"
        )

        # Act
        if CAN_ANONYMOUS_ACCESS_PUBLIC_DOCUMENT:
            result = persistent_query_periodic_table_api.upsert(
                persistent_query_periodic_table, AnonymousUser()
            )
            # Assert
            self.assertTrue(isinstance(result, PersistentQueryPeriodicTable))
            self.assertTrue(result.name, "new_persistent_query_periodic_table")

        else:
            with self.assertRaises(AccessControlError):
                persistent_query_periodic_table_api.upsert(
                    persistent_query_periodic_table, AnonymousUser()
                )


class TestPersistentQueryPeriodicTableGetAll(IntegrationBaseTestCase):
    """Test Persistent Query Periodic Table Get All"""

    fixture = fixture_persistent_query_periodic_table

    def test_get_all_as_superuser_returns_all_persistent_query_periodic_table(
        self,
    ):
        """test_get_all_as_superuser_returns_all_persistent_query_periodic_table"""

        # Arrange
        mock_user = create_mock_user("0", is_staff=True, is_superuser=True)

        # Act
        result = persistent_query_periodic_table_api.get_all(mock_user)

        # Assert
        self.assertTrue(len(result), 3)

    def test_get_all_as_user_raises_error(self):
        """test_get_all_as_user_raises_error"""

        # Arrange
        mock_user = create_mock_user("1")

        # Assert
        with self.assertRaises(AccessControlError):
            persistent_query_periodic_table_api.get_all(mock_user)

    def test_get_all_as_anonymous_user_raises_error(self):
        """test_get_all_as_anonymous_user_raises_error"""

        # Assert
        with self.assertRaises(AccessControlError):
            persistent_query_periodic_table_api.get_all(AnonymousUser())


class TestPersistentQueryPeriodicTableGetAllByUser(IntegrationBaseTestCase):
    """Test Persistent Query Periodic Table Get All By User"""

    fixture = fixture_persistent_query_periodic_table

    def test_get_all_by_user_as_superuser_returns_all_user_persistent_query_periodic_table(
        self,
    ):
        """test_get_all_by_user_as_superuser_returns_all_user_persistent_query_periodic_table"""

        # Arrange
        mock_user = create_mock_user("1", is_staff=True, is_superuser=True)

        # Act
        result = persistent_query_periodic_table_api.get_all_by_user(mock_user)

        # Assert
        self.assertTrue(len(result), 1)

    def test_get_all_by_user_returns_all_user_persistent_query_periodic_table(
        self,
    ):
        """test_get_all_by_user_returns_all_user_persistent_query_periodic_table"""

        # Arrange
        mock_user = create_mock_user("1")

        # Act
        result = persistent_query_periodic_table_api.get_all_by_user(mock_user)

        # Assert
        self.assertTrue(len(result), 1)

    def test_get_all_as_anonymous_user_raises_error(self):
        """test_get_all_as_anonymous_user_raises_error"""

        # Assert
        with self.assertRaises(AccessControlError):
            persistent_query_periodic_table_api.get_all_by_user(
                AnonymousUser()
            )
