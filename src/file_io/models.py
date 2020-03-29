from enum import Enum


class FileType(Enum):
    CSV = "csv"
    UNSUPPORTED = "unsupported"

    @classmethod
    def get_type_for_file_name(cls, file_name):
        if not file_name:
            return cls.UNSUPPORTED

        file_extension = file_name.split(".")[-1].lower()
        if file_extension == cls.CSV.value:
            return cls.CSV
        else:
            return cls.UNSUPPORTED
