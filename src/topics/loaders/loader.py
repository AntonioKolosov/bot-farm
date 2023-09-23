"""
Base Topics loaders class
"""


class Loader:
    def __init__(self, type: str) -> None:
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type

    def load_names(self) -> list[str]:
        """"""
        return list()

    def load_metadata(self, name: str) -> dict:
        """"""
        return {}

    def load_data_text(self, location: str) -> str:
        """"""
        return ""

    def load_data_json(self, location) -> dict:
        ''''''
        return {}

    def save_data_text(self, location, state: str) -> None:
        ''''''
