import logging
from enum import Enum

import settings
from file_io.exceptions import FileExtensionNotFoundException

LOGGER = logging.getLogger(__name__)


class FileOutputType(Enum):
    CSV = "csv"

    @classmethod
    def get_content_formatter(self, file_name: str):
        file_extension = file_name.split(".")[-1]

        if self.CSV.value == file_extension.lower():
            return csv_formatter
        else:
            raise FileExtensionNotFoundException(
                f"Unsupported file output format `{file_extension}`"
            )


def csv_formatter(contents):
    return ",".join(map(str, contents))


def write_to_file(file_name: str, contents):
    file_full_path = settings.CSV_DIR + file_name
    LOGGER.info(f"Adding new contents {file_full_path}")

    with open(file_full_path, "a") as output_file:
        content_formatter = FileOutputType.get_content_formatter(file_name)
        output_file.write(content_formatter(contents))
        output_file.close()
