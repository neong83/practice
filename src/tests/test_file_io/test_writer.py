from unittest.mock import mock_open, patch

from settings import CSV_DIR

from file_io.exceptions import FileExtensionNotFoundException
from file_io.writer import csv_formatter, get_content_formatter, write_to_file
from tests.base import TestCase


class WriteToFileTestCase(TestCase):
    def test_get_content_formatter_with_csv_format(self):
        FILE_NAME = "test.csv"
        self.assertEqual(get_content_formatter(FILE_NAME), csv_formatter)

    def test_get_content_formatter_with_case_insensitive(self):
        FILE_NAME = "TEST.CSV"
        self.assertEqual(get_content_formatter(FILE_NAME), csv_formatter)

    def test_get_content_formatter_with_extension_not_found_exception(self):
        FILE_NAME = "test.json"
        with self.assertRaises(FileExtensionNotFoundException):
            get_content_formatter(FILE_NAME)

    def test_csv_formatter_with_string(self):
        content = ["a", "b", "c"]
        self.assertEqual(csv_formatter(content), "a,b,c")

    def test_csv_formatter_with_int(self):
        content = [1, 2, 3]
        self.assertEqual(csv_formatter(content), "1,2,3")

    def test_csv_formatter_with_None(self):
        content = None
        self.assertEqual(csv_formatter(content), "")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_to_file(self, mock_file):
        FILE_NAME = "test.csv"
        write_to_file(FILE_NAME, [])
        mock_file.assert_called_with(CSV_DIR + FILE_NAME, "a")
