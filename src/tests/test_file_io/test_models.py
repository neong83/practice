from file_io.models import FileType
from tests.base import TestCase


class ModelsTestCase(TestCase):
    def test_get_type_for_file_name_with_csv(self):
        FILE_NAME = "test.csv"
        file_type = FileType.get_type_for_file_name(FILE_NAME)
        self.assertEqual(file_type, FileType.CSV)

    def test_get_type_for_file_name_with_unsupported(self):
        FILE_NAME = "test"
        file_type = FileType.get_type_for_file_name(FILE_NAME)
        self.assertEqual(file_type, FileType.UNSUPPORTED)

    def test_get_type_for_file_name_with_none(self):
        file_type = FileType.get_type_for_file_name(None)
        self.assertEqual(file_type, FileType.UNSUPPORTED)
