""" Unit tests for user-side forms
"""
from unittest import TestCase
from unittest.mock import patch

from django.core.exceptions import ValidationError
from django.test import RequestFactory

from core_explore_periodic_table_app.views.user.form import PeriodicTableForm
from core_main_app.commons.exceptions import QueryError
from core_main_app.utils.tests_tools.MockUser import create_mock_user


class TestPeriodicTableFormCleanElements(TestCase):
    """Test KeywordForm clean_keywords method"""

    def setUp(self) -> None:
        """setUp"""
        self.request = RequestFactory().post(
            "core_explore_periodic_table_index"
        )
        self.request.user = create_mock_user(user_id=1)

        self.keyword = "mock_keyword"
        self.form = PeriodicTableForm(
            request=self.request, data={"elements": self.keyword}
        )
        self.form.is_valid()

    @patch("core_explore_periodic_table_app.views.user.form.sanitize_value")
    def test_sanitize_value_function_is_called(self, mock_sanitize_value):
        """test_sanitize_value_function_is_called"""
        self.form.clean_elements()
        mock_sanitize_value.assert_called_with(self.keyword)

    @patch("core_explore_periodic_table_app.views.user.form.sanitize_value")
    def test_query_error_raises_validation_error(self, mock_sanitize_value):
        """test_query_error_raises_validation_error"""
        mock_sanitize_value.side_effect = QueryError("mock_query_error")

        with self.assertRaises(ValidationError):
            self.form.clean_elements()

    @patch("core_explore_periodic_table_app.views.user.form.sanitize_value")
    def test_sanitize_value_returns_cleaned_data(self, mock_sanitize_value):
        """test_sanitize_value_returns_cleaned_data"""
        mock_sanitize_value.return_value = self.keyword

        self.assertEquals(self.form.clean_elements(), self.keyword)
