""" Unit tests for periodic table admin views
"""

from unittest.case import TestCase

from django.http.request import HttpRequest
from unittest.mock import patch

from core_explore_periodic_table_app.views.admin import views as admin_views


class TestManagePeriodicTableIndexPost(TestCase):
    """Test Manage Periodic Table Index Post"""

    @patch.object(admin_views, "admin_render")
    @patch.object(admin_views, "messages")
    def test_manage_periodic_table_index_post(
        self, mock_messages, mock_admin_render
    ):
        """test_manage_periodic_table_index_post"""

        # Arrange
        request = HttpRequest()
        # Act
        admin_views._manage_periodic_table_index_post(request)
        mock_admin_render.assert_called()
