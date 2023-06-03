"""Startup module"""


class Startup:
    def __init__(self, type: str) -> None:
        """"""
        self.__type = type

    @property
    def type(self) -> str:
        """"""
        return self.__type
