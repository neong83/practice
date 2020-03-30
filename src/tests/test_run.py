from run import main_app
from unittest.mock import patch

from tests.base import TestCase


@patch("run.read_from_file")
@patch("run.write_to_file")
class RunTestCase(TestCase):
    def test_main_app_with_default_sorting(self, mock_write, mock_read):
        mock_read.return_value = ["ab", "za", "ba", "aa"]
        main_app("input", "output")
        mock_write.assert_called_once_with("output", ["za", "ba", "ab", "aa"])

    def test_main_app_with_none_ascii_character(self, mock_write, mock_read):
        mock_read.return_value = ["!", "*", "%"]
        main_app("input", "output")
        mock_write.assert_called_once_with("output", [])

    def test_main_app_with_number(self, mock_write, mock_read):
        mock_read.return_value = ["2", "66", "9"]
        main_app("input", "output")
        mock_write.assert_called_once_with("output", [])

    def test_main_app_with_letter_and_number_mix(self, mock_write, mock_read):
        mock_read.return_value = ["ab2", "b2c", "1aa"]
        main_app("input", "output")
        mock_write.assert_called_once_with("output", [])

    def test_main_app_for_words_with_extra_spaces(self, mock_write, mock_read):
        mock_read.return_value = [" abc ", "bz  ", "   ca"]
        main_app("input", "output")
        mock_write.assert_called_once_with("output", ["ca", "bz", "abc"])
