import logging
from enum import Enum

import settings

LOGGER = logging.getLogger(__name__)


class FileOutputType(Enum):
    CSV = "csv"

    def get_content_formatter(self):
        if self.CSV:
            return csv_formatter


def csv_formatter(contents):
    return ",".join(map(str, contents))


def write_to_file(
    file_name: str, contents, output_type: FileOutputType = FileOutputType.CSV
):
    file_full_path = settings.CSV_DIR + file_name
    LOGGER.info(f"Adding new contents {file_full_path}")

    with open(file_full_path, "a") as output_file:
        content_formatter = output_type.get_content_formatter()
        output_file.write(content_formatter(contents))
        output_file.close()
