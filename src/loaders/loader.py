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
        """Load all avaible files"""

    @abstractmethod
    def load_metadata(self, name: str) -> dict:
        """Load metadata"""

    @abstractmethod
    def load_content(self, ref: str) -> dict | str:
        """Load content"""
