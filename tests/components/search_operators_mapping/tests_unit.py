""" Unit tests for SearchOperatorMapping API calls.
"""
from unittest import TestCase, mock

from core_main_app.commons import exceptions
from core_explore_keyword_app.components.search_operator.models import (
    SearchOperator,
)
from core_explore_periodic_table_app.components.search_operator_mapping import (
    api as search_operator_mapping_api,
)
from core_explore_periodic_table_app.components.search_operator_mapping.models import (
    SearchOperatorMapping,
)


class TestsApiGetAll(TestCase):
    """Test Api Get All"""

    @mock.patch.object(SearchOperatorMapping, "get_all")
    def test_returns_no_error(self, mock_get_all):
        """test_returns_no_error"""

        expected_result = [
            "search_operator_mapping1",
            "search_operator_mapping2",
        ]
        mock_get_all.return_value = expected_result

        self.assertListEqual(
            search_operator_mapping_api.get_all(), expected_result
        )


class TestsApiGetById(TestCase):
    """Test Api Get By Id"""

    @mock.patch.object(SearchOperatorMapping, "get_by_id")
    def test_returns_no_error(self, mock_get_by_id):
        """test_returns_no_error"""

        expected_result = "search_operator_mapping"
        mock_get_by_id.return_value = expected_result

        self.assertEqual(
            search_operator_mapping_api.get_by_id("mock_id"), expected_result
        )

    @mock.patch.object(SearchOperatorMapping, "get_by_id")
    def test_incorrect_id_raises_api_error(self, mock_get_by_id):
        """test_incorrect_id_raises_api_error"""

        mock_get_by_id.side_effect = exceptions.ModelError(
            message="mock error"
        )

        with self.assertRaises(exceptions.ModelError):
            search_operator_mapping_api.get_by_id("mock_id")

    @mock.patch.object(SearchOperatorMapping, "get_by_id")
    def test_not_exist_raises_api_error(self, mock_get_by_id):
        """test_not_exist_raises_api_error"""

        mock_get_by_id.side_effect = exceptions.DoesNotExist(
            message="mock error"
        )

        with self.assertRaises(exceptions.DoesNotExist):
            search_operator_mapping_api.get_by_id("mock_id")


class TestsApiGetByName(TestCase):
    """Test Api Get By Name"""

    @mock.patch.object(SearchOperatorMapping, "get_by_search_operator_id")
    def test_returns_no_error(self, get_by_search_operator_id):
        """test_returns_no_error"""

        expected_result = "search_operator_mapping"
        get_by_search_operator_id.return_value = expected_result

        self.assertEqual(
            search_operator_mapping_api.get_by_search_operator_id("mock_id"),
            expected_result,
        )

    @mock.patch.object(SearchOperatorMapping, "get_by_search_operator_id")
    def test_not_exist_raises_api_error(self, get_by_search_operator_id):
        """test_not_exist_raises_api_error"""

        get_by_search_operator_id.side_effect = exceptions.DoesNotExist(
            message="mock error"
        )

        with self.assertRaises(exceptions.DoesNotExist):
            search_operator_mapping_api.get_by_search_operator_id("mock_name")


class TestsApiUpsert(TestCase):
    """Test Api Upsert"""

    def setUp(self) -> None:
        self.mock_search_operator_mapping = SearchOperatorMapping(
            search_operator=SearchOperator(
                name="mock_operator", xpath_list=["/x/path/a", "/x/path/b"]
            )
        )

    @mock.patch.object(SearchOperatorMapping, "save")
    def test_returns_no_error(self, mock_save):
        """test_returns_no_error"""

        mock_save.return_value = None
        search_operator_mapping_api.upsert(self.mock_search_operator_mapping)

    @mock.patch.object(SearchOperatorMapping, "save")
    def test_duplicate_raises_api_error(self, mock_save):
        """test_duplicate_raises_api_error"""

        mock_save.side_effect = exceptions.NotUniqueError(message="mock error")

        with self.assertRaises(exceptions.NotUniqueError):
            search_operator_mapping_api.upsert(
                self.mock_search_operator_mapping
            )


class TestsApiDelete(TestCase):
    """Test Api Delete"""

    @mock.patch.object(SearchOperatorMapping, "delete")
    def test_returns_no_error(self, mock_delete):
        """test_returns_no_error"""

        mock_delete.return_value = None

        self.assertEqual(
            search_operator_mapping_api.delete(SearchOperatorMapping()), None
        )
