from run import read_csv_from_file
from tests.base import TestCase


class TestCSV(TestCase):
    def test_read_csv_from_file_name_with_string_csv(self):
        FILE_NAME = "csv/test_string_input.csv"
        contents = read_csv_from_file(FILE_NAME)
        self.assertNotEqual(contents, [])
        self.assertTrue("Wiki" in contents)

    def test_read_csv_from_file_name_with_file_not_found(self):
        FILE_NAME = "csv/NO_EXIST_FILE.csv"
        with self.assertLogs(level="WARNING") as cm:
            self.assertEqual(read_csv_from_file(FILE_NAME), [])
        self.assertRegexIn("unable to find file", cm.output)
