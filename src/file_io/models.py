class BaseFileType:
    CSV = "csv"

    @classmethod
    def get_file_extension(cls, file_name: str) -> str:
        return file_name.split(".")[-1]
