import logging
from abc import ABC, abstractmethod
from string import ascii_letters

from sorting.algorithms.hash_map import (
    AlphabetIndexCoefficient,
    hash_first_character_from_word,
)
from sorting.algorithms.insertion import get_insert_position_form_sorted_array

LOGGER = logging.getLogger(__name__)


class BaseStructure(ABC):  # pragma: no cover
    @abstractmethod
    def add(self, value):
        pass

    @abstractmethod
    def list(self):
        pass


class DescendingHashList(BaseStructure):
    def __init__(self):
        self.__accident = False
        self.buckets = [[] for _ in range(26)]
        self.hash_algorithm = AlphabetIndexCoefficient(acceding=self.__accident)

    def is_ascii_letters(self, value):
        for letter in value:
            if letter not in ascii_letters:
                return False
        return True

    def add(self, value: str):
        LOGGER.info(f"Adding `{value}` to bucket")

        if value:
            value = value.strip()

        if not value or not self.is_ascii_letters(value):
            LOGGER.warning(f"Found none ASCII letter(s) in {value}, skip insert")
            return

        hash_value = hash_first_character_from_word(self.hash_algorithm, value)
        position = get_insert_position_form_sorted_array(
            self.buckets[hash_value], value, self.__accident
        )
        self.buckets[hash_value].insert(position, value)

    def list(self):
        result = []
        for bucket in self.buckets:
            result += bucket
        return result
