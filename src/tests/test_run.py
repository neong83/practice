from run import main_app
from unittest.mock import patch

from tests.base import TestCase


class RunTestCase(TestCase):
    @patch("run.read_from_file")
    @patch("run.write_to_file")
    def test_main_app_with_default_sorting(self, mock_write, mock_read):
        mock_read.return_value = ["ab", "za", "ba", "aa"]
        main_app("input", "output")
        mock_write.assert_called_once_with("output", ["za", "ba", "ab", "aa"])
