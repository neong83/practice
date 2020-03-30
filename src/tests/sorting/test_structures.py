from string import ascii_lowercase

from sorting.structures import DescendingHashList
from tests.base import TestCase


class DescendingHashListTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.hashed_list = DescendingHashList()

    def tearDown(self) -> None:
        for bucket in self.hashed_list.buckets:
            bucket.clear()

    def get_charachter_index(self, character):
        index = ascii_lowercase.index(character)
        return 25 - index

    def test_is_ascii_letter(self):
        self.assertTrue(self.hashed_list.is_ascii_letters("abc"))

    def test_is_ascii_letter_with_number(self):
        self.assertFalse(self.hashed_list.is_ascii_letters("456"))

    def test_is_ascii_letter_with_alphabet_and_number(self):
        self.assertFalse(self.hashed_list.is_ascii_letters("a1b2"))

    def test_add(self):
        bucket_index = self.get_charachter_index("a")
        self.hashed_list.buckets[bucket_index] = ["ac", "ab", "aa"]
        self.hashed_list.add("ad")
        self.assertEqual(
            self.hashed_list.buckets[bucket_index], ["ad", "ac", "ab", "aa"]
        )

    def test_add_with_None(self):
        with self.assertLogs(level="WARNING") as cm:
            self.hashed_list.add(None)
        self.assertRegexIn("Found none ASCII letter", cm.output)

    def test_to_list(self):
        BUCKET_VALUE_SET_ONE = ["ab", "ac"]
        BUCKET_VALUE_SET_TWO = ["ba", "bb"]
        self.hashed_list.buckets[0] = BUCKET_VALUE_SET_ONE
        self.hashed_list.buckets[3] = BUCKET_VALUE_SET_TWO
        self.assertEqual(
            self.hashed_list.to_list(), BUCKET_VALUE_SET_ONE + BUCKET_VALUE_SET_TWO
        )
