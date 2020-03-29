import logging

import settings
from file_io.exceptions import FileExtensionNotFoundException
from file_io.models import FileType

LOGGER = logging.getLogger(__name__)


def get_content_formatter(file_name: str):
    if FileType.is_csv(file_name):
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
    LOGGER.info(f"Adding new contents {file_full_path}")

    content_formatter = get_content_formatter(file_name)
    with open(file_full_path, "a") as output_file:
        output_file.write(content_formatter(contents))
        output_file.close()
