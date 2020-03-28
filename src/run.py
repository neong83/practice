import csv
import logging
from typing import List

LOGGER = logging.getLogger(__name__)


def read_csv_from_file(file_name: str) -> List[str]:
    contents = []
    try:
        with open(file_name, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                contents += row
    except FileNotFoundError:
        LOGGER.warning(f"unable to find file in {file_name}")

    return contents
