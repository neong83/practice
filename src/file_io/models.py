class FileType:
    CSV = "csv"

    @classmethod
    def __get_file_extension(cls, file_name: str) -> str:
        return file_name.split(".")[-1]

    @classmethod
    def is_csv_file(cls, file_name) -> bool:
        return cls.__get_file_extension(file_name).lower() == cls.CSV
