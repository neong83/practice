import logging

import settings

from file_io.exceptions import FileExtensionNotFoundException
from file_io.models import FileType

LOGGER = logging.getLogger(__name__)


def get_content_formatter(file_name: str):
    file_type = FileType.get_type_for_file_name(file_name)
    if file_type == FileType.CSV:
        return csv_formatter
    else:
        raise FileExtensionNotFoundException(
            f"Unsupported file output format `{file_name}`"
        )


def csv_formatter(contents):
    if contents:
        return ",".join(map(str, contents))
    return ""


def write_to_file(file_name: str, contents):
    file_full_path = settings.CSV_DIR + file_name
    LOGGER.info(f"Adding new contents to {file_full_path}")

    content_formatter = get_content_formatter(file_name)
    with open(file_full_path, "a") as output_file:
        output_file.write(content_formatter(contents) + "\n")
        output_file.close()
