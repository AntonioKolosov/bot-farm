"""
Base Topics loaders class
"""


from abc import abstractmethod


class Loader:
    def __init__(self, type: str) -> None:
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type

    @abstractmethod
    def load_names(self) -> list[str]:
        """"""

    @abstractmethod
    def load_metadata(self, name: str) -> dict:
        """"""

    @abstractmethod
    def load_content(self, type: str, ref: str) -> str:
        """"""

    @abstractmethod
    def load_index(self, type: str, ref: str) -> dict:
        ''''''
    @abstractmethod
    def load_state(self, type: str, ref: str) -> str:
        """"""

    def save_state(self, type: str, ref: str, state: str) -> None:
        ''''''
