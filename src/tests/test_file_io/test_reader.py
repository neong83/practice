from unittest.mock import mock_open, patch

from file_io.exceptions import FileExtensionNotFoundException
from file_io.reader import get_file_reader, read_csv_file, read_from_file
from settings import CSV_DIR
from tests.base import TestCase


class ReaderTestCase(TestCase):
    def test_get_file_reader_with_csv_format(self):
        FILE_NAME = "test.csv"
        self.assertEqual(get_file_reader(FILE_NAME), read_csv_file)

    def test_get_file_reader_with_case_insensitive(self):
        FILE_NAME = "TEST.CSV"
        self.assertEqual(get_file_reader(FILE_NAME), read_csv_file)

    def test_get_file_reader_with_extension_not_found_exception(self):
        FILE_NAME = "test.json"
        with self.assertRaises(FileExtensionNotFoundException):
            get_file_reader(FILE_NAME)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="Code,Action,Pull\nWiki,Insight",
    )
    def test_read_csv_file(self, mock_file):
        contents = read_csv_file("test_path")
        self.assertTrue("Wiki" in contents)

    def test_read_csv_file_with_exception(self):
        with self.assertLogs(level="WARNING") as cm:
            contents = read_csv_file("test_path")
            self.assertEqual(contents, [])
        self.assertRegexIn("Unable to find file", cm.output)

    @patch("file_io.reader.read_csv_file")
    def test_read_from_file_with_csv_file(self, mock_read_csv_file):
        FILE_NAME = "test.csv"
        read_from_file(FILE_NAME)
        mock_read_csv_file.assert_called_once_with(CSV_DIR + FILE_NAME)
