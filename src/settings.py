import logging

from sorting.structures import BaseStructure, DescendingHashList

logging.basicConfig(
    level=logging.INFO, format="%(levelname)s %(asctime)s %(module)s %(message)s"
)
CSV_DIR = "csv/"
INPUT_FILE = "input.csv"
DEFAULT_SORT_FUNC: BaseStructure = DescendingHashList
