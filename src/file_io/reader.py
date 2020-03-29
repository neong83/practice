import csv
import logging
from typing import List

import settings
from file_io.exceptions import FileExtensionNotFoundException
from file_io.models import BaseFileType

LOGGER = logging.getLogger(__name__)


class FileInputType(BaseFileType):
    @classmethod
    def get_file_reader(cls, file_name: str):
        file_extension = cls.get_file_extension(file_name)
        if cls.CSV == file_extension.lower():
            return read_csv_file
        else:
            raise FileExtensionNotFoundException(
                f"Unable to read from '{file_extension}"
            )


def read_csv_file(file_path: str) -> List[str]:
    LOGGER.info("Loading file with CSV reader")
    contents = []
    try:
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                contents += row
    except FileNotFoundError:
        LOGGER.warning(f"Unable to find file in {file_path}")

    return contents


def read_from_file(file_name: str):
    file_full_path = settings.CSV_DIR + file_name
    read = FileInputType.get_file_reader(file_name)

    LOGGER.info(f"Reading from {file_full_path}")
    return read(file_full_path)
