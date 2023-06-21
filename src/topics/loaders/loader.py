"""
Topics loader
"""

from ..schemas.topic import Topic


class Loader:
    def __init__(self, type: str) -> None:
        self.__type = type
        self.__metadata: list[Topic] = []

    @property
    def type(self) -> str:
        return self.__type

    @property
    def metadata(self) -> list[Topic]:
        return self.__metadata

    def __load_metadata(self) -> None:
        """"""
