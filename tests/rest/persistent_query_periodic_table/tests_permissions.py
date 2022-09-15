""" Authentication tests for PersistentQueryPeriodicTable REST API.
"""
from unittest.mock import patch

from django.contrib.auth.models import AnonymousUser
from django.test import SimpleTestCase
from rest_framework import status

from core_main_app.utils.tests_tools.MockUser import create_mock_user
from core_main_app.utils.tests_tools.RequestMock import RequestMock

import core_explore_periodic_table_app.components.persistent_query_periodic_table.api as persistent_query_periodic_table_api
from core_explore_periodic_table_app.components.persistent_query_periodic_table.models import (
    PersistentQueryPeriodicTable,
)
from core_explore_periodic_table_app.rest.persistent_query_periodic_table import (
    views as persistent_query_periodic_table_views,
)
from core_explore_periodic_table_app.rest.persistent_query_periodic_table.serializers import (
    PersistentQueryPeriodicTableSerializer,
    PersistentQueryPeriodicTableAdminSerializer,
)


class TestAdminPersistentQueryPeriodicTableListGet(SimpleTestCase):
    """Test Admin Persistent Query Periodic Table List Get"""

    def test_anonymous_returns_http_403(self):
        """test_anonymous_returns_http_403"""

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
            AnonymousUser(),
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_returns_http_403(self):
        """test_authenticated_returns_http_403"""

        mock_user = create_mock_user("1")

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
            mock_user,
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch.object(PersistentQueryPeriodicTable, "get_all")
    def test_superuser_returns_http_200(self, get_all):
        """test_superuser_returns_http_200"""

        get_all.return_value = {}
        mock_user = create_mock_user("1", is_staff=True, is_superuser=True)

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
            mock_user,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPersistentQueryPeriodicTableListGet(SimpleTestCase):
    """Test Persistent Query Periodic Table List Get"""

    def test_anonymous_returns_http_403(self):
        """test_anonymous_returns_http_403"""

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableList.as_view(),
            AnonymousUser(),
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch.object(PersistentQueryPeriodicTable, "get_all_by_user")
    def test_authenticated_returns_http_200(self, get_all):
        """test_authenticated_returns_http_200"""

        get_all.return_value = {}
        mock_user = create_mock_user("1")

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableList.as_view(),
            mock_user,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch.object(PersistentQueryPeriodicTable, "get_all_by_user")
    def test_superuser_returns_http_200(self, get_all):
        """test_superuser_returns_http_200"""

        get_all.return_value = {}
        mock_user = create_mock_user("1", is_staff=True, is_superuser=True)

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableList.as_view(),
            mock_user,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPersistentQueryPeriodicTableListPost(SimpleTestCase):
    """Test Persistent Query Periodic Table List Post"""

    def test_anonymous_returns_http_403(self):
        """test_anonymous_returns_http_403"""

        response = RequestMock.do_request_post(
            persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
            AnonymousUser(),
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch.object(PersistentQueryPeriodicTableSerializer, "is_valid")
    @patch.object(PersistentQueryPeriodicTableSerializer, "save")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_authenticated_returns_http_201(
        self,
        persistent_query_periodic_table_serializer_data,
        persistent_query_periodic_table_serializer_save,
        persistent_query_periodic_table_serializer_is_valid,
    ):
        """test_authenticated_returns_http_201"""

        persistent_query_periodic_table_serializer_is_valid.return_value = True
        persistent_query_periodic_table_serializer_save.return_value = None
        persistent_query_periodic_table_serializer_data.return_value = {}
        mock_user = create_mock_user("1")

        response = RequestMock.do_request_post(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableList.as_view(),
            mock_user,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @patch.object(PersistentQueryPeriodicTableAdminSerializer, "is_valid")
    @patch.object(PersistentQueryPeriodicTableAdminSerializer, "save")
    @patch.object(PersistentQueryPeriodicTableAdminSerializer, "data")
    def test_superuser_returns_http_201(
        self,
        persistent_query_periodic_table_serializer_data,
        persistent_query_periodic_table_serializer_save,
        persistent_query_periodic_table_serializer_is_valid,
    ):
        """test_superuser_returns_http_201"""

        persistent_query_periodic_table_serializer_is_valid.return_value = True
        persistent_query_periodic_table_serializer_save.return_value = None
        persistent_query_periodic_table_serializer_data.return_value = {}

        mock_user = create_mock_user("1", is_staff=True, is_superuser=True)

        response = RequestMock.do_request_post(
            persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
            mock_user,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestAdminPersistentQueryPeriodicTableListPost(SimpleTestCase):
    """Test Admin Persistent Query Periodic Table List Post"""

    def test_anonymous_returns_http_403(self):
        """test_anonymous_returns_http_403"""

        response = RequestMock.do_request_post(
            persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
            AnonymousUser(),
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_returns_http_403(self):
        """test_authenticated_returns_http_403"""

        mock_user = create_mock_user("1")

        response = RequestMock.do_request_post(
            persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
            mock_user,
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch.object(PersistentQueryPeriodicTableAdminSerializer, "is_valid")
    @patch.object(PersistentQueryPeriodicTableAdminSerializer, "save")
    @patch.object(PersistentQueryPeriodicTableAdminSerializer, "data")
    def test_superuser_returns_http_201(
        self,
        persistent_query_periodic_table_serializer_data,
        persistent_query_periodic_table_serializer_save,
        persistent_query_periodic_table_serializer_is_valid,
    ):
        """test_superuser_returns_http_201"""

        persistent_query_periodic_table_serializer_is_valid.return_value = True
        persistent_query_periodic_table_serializer_save.return_value = None
        persistent_query_periodic_table_serializer_data.return_value = {}

        mock_user = create_mock_user("1", is_staff=True, is_superuser=True)

        response = RequestMock.do_request_post(
            persistent_query_periodic_table_views.AdminPersistentQueryPeriodicTableList.as_view(),
            mock_user,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestPersistentQueryPeriodicTableDetailGet(SimpleTestCase):
    """Test Persistent Query Periodic Table Detail Get"""

    @patch.object(persistent_query_periodic_table_api, "get_by_id")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_anonymous_returns_http_403(
        self,
        mock_persistent_query_periodic_table_serializer_data,
        mock_persistent_query_periodic_table_api_get_by_id,
    ):
        """test_anonymous_returns_http_403"""

        mock_persistent_query_periodic_table_serializer_data.return_value = {}
        mock_persistent_query_periodic_table_api_get_by_id.return_value = None
        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            AnonymousUser(),
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch.object(persistent_query_periodic_table_api, "get_by_id")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_authenticated_returns_http_200(
        self,
        mock_persistent_query_periodic_table_serializer_data,
        mock_persistent_query_periodic_table_api_get_by_id,
    ):
        """test_authenticated_returns_http_200"""

        mock_persistent_query_periodic_table_serializer_data.return_value = {}
        mock_persistent_query_periodic_table_api_get_by_id.return_value = None
        mock_user = create_mock_user("1")

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            mock_user,
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch.object(persistent_query_periodic_table_api, "get_by_id")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_superuser_returns_http_200(
        self,
        mock_persistent_query_periodic_table_serializer_data,
        mock_persistent_query_periodic_table_api_get_by_id,
    ):
        """test_superuser_returns_http_200"""

        mock_persistent_query_periodic_table_serializer_data.return_value = {}
        mock_persistent_query_periodic_table_api_get_by_id.return_value = None
        mock_user = create_mock_user("1", is_staff=True)

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            mock_user,
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPersistentQueryPeriodicTableDetailPatch(SimpleTestCase):
    """Test Persistent Query Periodic Table Detail Patch"""

    def test_anonymous_returns_http_403(self):
        """test_anonymous_returns_http_403"""

        response = RequestMock.do_request_patch(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            AnonymousUser(),
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch.object(persistent_query_periodic_table_api, "get_by_id")
    @patch.object(PersistentQueryPeriodicTableSerializer, "is_valid")
    @patch.object(PersistentQueryPeriodicTableSerializer, "save")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_authenticated_returns_http_200(
        self,
        mock_persistent_query_periodic_table_data,
        mock_persistent_query_periodic_table_save,
        mock_persistent_query_periodic_table_is_valid,
        mock_persistent_query_periodic_table_api_get_by_id,
    ):
        """test_authenticated_returns_http_200"""

        mock_persistent_query_periodic_table_data.return_value = {}
        mock_persistent_query_periodic_table_save.return_value = None
        mock_persistent_query_periodic_table_is_valid.return_value = True
        mock_persistent_query_periodic_table_api_get_by_id.return_value = None
        mock_user = create_mock_user("1")

        response = RequestMock.do_request_patch(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            mock_user,
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch.object(persistent_query_periodic_table_api, "get_by_id")
    @patch.object(PersistentQueryPeriodicTableSerializer, "is_valid")
    @patch.object(PersistentQueryPeriodicTableSerializer, "save")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_superuser_returns_http_200(
        self,
        mock_persistent_query_periodic_table_data,
        mock_persistent_query_periodic_table_save,
        mock_persistent_query_periodic_table_is_valid,
        mock_persistent_query_periodic_table_api_get_by_id,
    ):
        """test_superuser_returns_http_200"""

        mock_persistent_query_periodic_table_data.return_value = {}
        mock_persistent_query_periodic_table_save.return_value = None
        mock_persistent_query_periodic_table_is_valid.return_value = True
        mock_persistent_query_periodic_table_api_get_by_id.return_value = None
        mock_user = create_mock_user("1", is_staff=True)

        response = RequestMock.do_request_patch(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            mock_user,
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPersistentQueryPeriodicTableDetailDelete(SimpleTestCase):
    """Test Persistent Query Periodic Table Detail Delete"""

    def test_anonymous_returns_http_403(self):
        """test_anonymous_returns_http_403"""

        response = RequestMock.do_request_delete(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            AnonymousUser(),
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch.object(persistent_query_periodic_table_api, "get_by_id")
    @patch.object(persistent_query_periodic_table_api, "delete")
    def test_authenticated_returns_http_200(
        self,
        persistent_query_periodic_table_api_delete,
        persistent_query_periodic_table_get_by_id,
    ):
        """test_authenticated_returns_http_200"""

        persistent_query_periodic_table_api_delete.return_value = None
        persistent_query_periodic_table_get_by_id.return_value = None
        mock_user = create_mock_user("1")

        response = RequestMock.do_request_delete(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            mock_user,
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @patch.object(persistent_query_periodic_table_api, "get_by_id")
    @patch.object(persistent_query_periodic_table_api, "delete")
    def test_superuser_returns_http_200(
        self,
        persistent_query_periodic_table_api_delete,
        persistent_query_periodic_table_get_by_id,
    ):
        """test_superuser_returns_http_200"""

        persistent_query_periodic_table_api_delete.return_value = None
        persistent_query_periodic_table_get_by_id.return_value = None
        mock_user = create_mock_user("1", is_staff=True)

        response = RequestMock.do_request_delete(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableDetail.as_view(),
            mock_user,
            param={"pk": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestPersistentQueryPeriodicTableByNameGet(SimpleTestCase):
    """Test Persistent Query Periodic Table By Name Get"""

    @patch.object(persistent_query_periodic_table_api, "get_by_name")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_anonymous_returns_http_403(
        self,
        mock_persistent_query_periodic_table_serializer_data,
        mock_persistent_query_periodic_table_api_get_by_name,
    ):
        """test_anonymous_returns_http_403"""

        mock_persistent_query_periodic_table_serializer_data.return_value = {}
        mock_persistent_query_periodic_table_api_get_by_name.return_value = None
        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableByName.as_view(),
            AnonymousUser(),
            param={"name": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch.object(persistent_query_periodic_table_api, "get_by_name")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_authenticated_returns_http_200(
        self,
        mock_persistent_query_periodic_table_serializer_data,
        mock_persistent_query_periodic_table_api_get_by_name,
    ):
        """test_authenticated_returns_http_200"""

        mock_persistent_query_periodic_table_serializer_data.return_value = {}
        mock_persistent_query_periodic_table_api_get_by_name.return_value = None
        mock_user = create_mock_user("1")

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableByName.as_view(),
            mock_user,
            param={"name": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch.object(persistent_query_periodic_table_api, "get_by_name")
    @patch.object(PersistentQueryPeriodicTableSerializer, "data")
    def test_superuser_returns_http_200(
        self,
        mock_persistent_query_periodic_table_serializer_data,
        mock_persistent_query_periodic_table_api_get_by_name,
    ):
        """test_superuser_returns_http_200"""

        mock_persistent_query_periodic_table_serializer_data.return_value = {}
        mock_persistent_query_periodic_table_api_get_by_name.return_value = None
        mock_user = create_mock_user("1", is_staff=True)

        response = RequestMock.do_request_get(
            persistent_query_periodic_table_views.PersistentQueryPeriodicTableByName.as_view(),
            mock_user,
            param={"name": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
