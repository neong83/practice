from run import read_csv_from_file
from tests.base import TestCase


class TestCSV(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.FILE_NAME = "csv/test_string_input.csv"

    def test_read_csv_from_file_name(self):
        contents = read_csv_from_file(self.FILE_NAME)
        self.assertNotEqual(contents, [])

    def test_read_csv_from_file_name_with_expected_content(self):
        contents = read_csv_from_file(self.FILE_NAME)
        self.assertTrue("Wiki" in contents)

    def test_read_csv_from_file_name_with_file_not_found(self):
        FILE_NAME = "csv/NO_EXIST_FILE.csv"
        with self.assertLogs(level="WARNING") as cm:
            self.assertEqual(read_csv_from_file(FILE_NAME), [])
        self.assertRegexIn("unable to find file", cm.output)
