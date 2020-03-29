from unittest.mock import mock_open, patch

from file_io.writer import FileOutputType, csv_formatter, write_to_file
from settings import CSV_DIR
from tests.base import TestCase


class FileOutputTypeTestCase(TestCase):
    def test_get_content_formatter(self):
        formatter = FileOutputType.CSV
        self.assertEqual(formatter.get_content_formatter(), csv_formatter)


class FormatterTestCase(TestCase):
    def test_csv_formatter_with_string(self):
        content = ["a", "b", "c"]
        self.assertEqual(csv_formatter(content), "a,b,c")

    def test_csv_formatter_with_int(self):
        content = [1, 2, 3]
        self.assertEqual(csv_formatter(content), "1,2,3")


class WriteToFileTestCase(TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_write_to_file(self, mock_file):
        write_to_file("test", [])
        mock_file.assert_called_with(CSV_DIR + "test", "a")
