import logging
from abc import ABC, abstractmethod
from string import ascii_lowercase

LOGGER = logging.getLogger(__name__)


class BaseHashCoefficient(ABC):  # pragma: no cover
    @abstractmethod
    def get_coefficient(self, character):
        pass


class AlphabetIndexCoefficient(BaseHashCoefficient):
    TOTAL_NUMBER_ALPHABET = 26

    def __init__(self, acceding: bool = False):
        super().__init__()
        self.acceding = acceding

    def get_coefficient(self, character):
        index = ascii_lowercase.index(character)
        if not self.acceding:
            return self.TOTAL_NUMBER_ALPHABET - index - 1
        return index


def hash_first_character_from_word(algorithm: BaseHashCoefficient, word: str) -> int:
    LOGGER.info(f"Hashing first character for `{word}`")
    if not word:
        LOGGER.warning("Skip hashing for `None`")
        return None

    first_character = word[0].lower()
    return algorithm.get_coefficient(first_character)
