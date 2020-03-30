import settings

from file_io.reader import read_from_file
from file_io.writer import write_to_file


def main_app(input_file_name: str, output_file_name: str):
    contents = read_from_file(input_file_name)

    sort_func_class = settings.DEFAULT_SORT_FUNC
    sort_func = sort_func_class()

    [sort_func.add(value) for value in contents]
    write_to_file(output_file_name, sort_func.list())


main_app("input.csv", "output.csv")  # pragma: no cover
