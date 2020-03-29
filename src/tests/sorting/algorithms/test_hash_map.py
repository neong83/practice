from sorting.algorithms.hash_map import (
    AlphabetIndexCoefficient,
    hash_first_character_from_word,
)
from tests.base import TestCase


class HashMapTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.algorithm = AlphabetIndexCoefficient()

    def test_get_coefficient_with_acceding(self):
        self.algorithm.acceding = True
        self.assertEqual(self.algorithm.get_coefficient("a"), 0)

    def test_get_coefficient_with_descending(self):
        self.algorithm.acceding = False
        self.assertEqual(self.algorithm.get_coefficient("a"), 25)

    def test_first_character_from_word_accident_with_lower_case_words(self):
        self.algorithm.acceding = True
        index = hash_first_character_from_word(self.algorithm, "alphabet")
        self.assertEqual(index, 0)

    def test_first_character_from_word_accident_with_upper_case_words(self):
        self.algorithm.acceding = True
        index = hash_first_character_from_word(self.algorithm, "ALPHABET")
        self.assertEqual(index, 0)

    def test_first_character_from_word_descending_with_lower_case_words(self):
        self.algorithm.acceding = False
        index = hash_first_character_from_word(self.algorithm, "alphabet")
        self.assertEqual(index, 25)

    def test_first_character_from_word_descending_with_uppper_case_words(self):
        self.algorithm.acceding = False
        index = hash_first_character_from_word(self.algorithm, "ALPHABET")
        self.assertEqual(index, 25)

    def test_first_character_from_word_accident_with_None(self):
        self.algorithm.acceding = True
        index = hash_first_character_from_word(self.algorithm, None)
        self.assertIsNone(index)
