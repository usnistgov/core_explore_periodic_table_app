""" Unit tests for SearchOperatorMapping API calls.
"""
from unittest import TestCase, mock

from core_explore_periodic_table_app.components.search_operator_mapping import (
    api as search_operator_mapping_api,
)
from core_explore_periodic_table_app.components.search_operator_mapping.models import (
    SearchOperatorMapping,
)
from core_main_app.commons import exceptions


class TestsApiGetAll(TestCase):
    @mock.patch.object(SearchOperatorMapping, "get_all")
    def test_returns_no_error(self, mock_get_all):
        expected_result = ["search_operator_mapping1", "search_operator_mapping2"]
        mock_get_all.return_value = expected_result

        self.assertListEqual(search_operator_mapping_api.get_all(), expected_result)


class TestsApiGetById(TestCase):
    @mock.patch.object(SearchOperatorMapping, "get_by_id")
    def test_returns_no_error(self, mock_get_by_id):
        expected_result = "search_operator_mapping"
        mock_get_by_id.return_value = expected_result

        self.assertEqual(
            search_operator_mapping_api.get_by_id("mock_id"), expected_result
        )

    @mock.patch.object(SearchOperatorMapping, "get_by_id")
    def test_incorrect_id_raises_api_error(self, mock_get_by_id):
        mock_get_by_id.side_effect = exceptions.ModelError(message="mock error")

        with self.assertRaises(exceptions.ModelError):
            search_operator_mapping_api.get_by_id("mock_id")

    @mock.patch.object(SearchOperatorMapping, "get_by_id")
    def test_nonexistant_raises_api_error(self, mock_get_by_id):
        mock_get_by_id.side_effect = exceptions.DoesNotExist(message="mock error")

        with self.assertRaises(exceptions.DoesNotExist):
            search_operator_mapping_api.get_by_id("mock_id")


class TestsApiGetByName(TestCase):
    @mock.patch.object(SearchOperatorMapping, "get_by_search_operator_id")
    def test_returns_no_error(self, get_by_search_operator_id):
        expected_result = "search_operator_mapping"
        get_by_search_operator_id.return_value = expected_result

        self.assertEqual(
            search_operator_mapping_api.get_by_search_operator_id("mock_id"),
            expected_result,
        )

    @mock.patch.object(SearchOperatorMapping, "get_by_search_operator_id")
    def test_nonexistant_raises_api_error(self, get_by_search_operator_id):
        get_by_search_operator_id.side_effect = exceptions.DoesNotExist(
            message="mock error"
        )

        with self.assertRaises(exceptions.DoesNotExist):
            search_operator_mapping_api.get_by_search_operator_id("mock_name")


class TestsApiUpsert(TestCase):
    def setUp(self) -> None:
        self.mock_search_operator_mapping = SearchOperatorMapping(
            search_operator="mock_id"
        )

    @mock.patch.object(SearchOperatorMapping, "save")
    def test_returns_no_error(self, mock_save):
        mock_save.return_value = None

        self.assertEqual(
            search_operator_mapping_api.upsert(self.mock_search_operator_mapping), None
        )

    @mock.patch.object(SearchOperatorMapping, "save")
    def test_duplicate_raises_api_error(self, mock_save):
        mock_save.side_effect = exceptions.NotUniqueError(message="mock error")

        with self.assertRaises(exceptions.NotUniqueError):
            search_operator_mapping_api.upsert(self.mock_search_operator_mapping)


class TestsApiDelete(TestCase):
    @mock.patch.object(SearchOperatorMapping, "delete")
    def test_returns_no_error(self, mock_delete):
        mock_delete.return_value = None

        self.assertEqual(
            search_operator_mapping_api.delete(SearchOperatorMapping()), None
        )
