from sorting.algorithms.insertion import (
    get_insert_position_form_sorted_array,
    search_insert_position_with_accident_sorted_array,
    search_insert_position_with_descending_sorted_array,
)
from tests.base import TestCase
from unittest.mock import patch


class InsertionTestCase(TestCase):
    def test_get_insert_position_form_sorted_array_with_empty_array(self):
        index = get_insert_position_form_sorted_array([], "a")
        self.assertEqual(index, 0)

    @patch(
        "sorting.algorithms.insertion.search_insert_position_with_accident_sorted_array"
    )
    def test_get_insert_position_from_sorted_array_with_accident_array(
        self, mock_search
    ):
        TEST_ARRAY = ["abc"]
        NEW_WORD = ["ab"]

        get_insert_position_form_sorted_array(TEST_ARRAY, NEW_WORD, accident=True)
        mock_search.assert_called_once_with(TEST_ARRAY, NEW_WORD)

    @patch(
        "sorting.algorithms.insertion.search_insert_position_with_descending_sorted_array"
    )
    def test_get_insert_position_from_sorted_array_with_accident_array(
        self, mock_search
    ):
        TEST_ARRAY = ["abc"]
        NEW_WORD = ["ab"]

        get_insert_position_form_sorted_array(TEST_ARRAY, NEW_WORD)
        mock_search.assert_called_once_with(TEST_ARRAY, NEW_WORD)

    def test_search_insert_position_with_descending_sorted_array_with_upper_case_word(
        self,
    ):
        index = search_insert_position_with_descending_sorted_array(["Aa"], "Ba")
        self.assertEqual(index, 0)

    def test_search_insert_position_with_descending_sorted_array_with_mix_word_test_set_one(
        self,
    ):
        index = search_insert_position_with_descending_sorted_array(["Aa"], "ba")
        self.assertEqual(index, 0)

    def test_search_insert_position_with_descending_sorted_array_with_mix_word_test_set_two(
        self,
    ):
        index = search_insert_position_with_descending_sorted_array(["aa"], "Ba")
        self.assertEqual(index, 1)

    def test_search_insert_position_with_descending_sorted_array_with_mix_word_test_set_three(
        self,
    ):
        index = search_insert_position_with_descending_sorted_array(["aa"], "Aa")
        self.assertEqual(index, 1)

    def test_search_insert_position_with_descending_sorted_array_with_mix_word_test_set_four(
        self,
    ):
        index = search_insert_position_with_descending_sorted_array(["Aa"], "aa")
        self.assertEqual(index, 0)

    def test_search_insert_position_with_descending_sorted_array_with_mix_word_test_set_five(
        self,
    ):
        index = search_insert_position_with_descending_sorted_array(["ac", "aa"], "ab")
        self.assertEqual(index, 1)

    def test_search_insert_position_with_accident_sorted_array_with_error(self):
        with self.assertRaises(NotImplementedError):
            search_insert_position_with_accident_sorted_array([], "a")
