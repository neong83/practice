import csv
from typing import List


def read_csv_from_file(file_name: str) -> List[str]:
    contents = []
    try:
        with open(file_name, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                contents.append(row)
    except FileNotFoundError:
        print(f"unable to find {file_name}")

    return contents
