"""
"""

import os
from .schemas.topic import Topic
from .loaders.loader import Loader
from .loaders.fsloader import FsLoader


class TopicsList:
    """"
    """
    def __init__(self) -> None:
        loader_type = os.environ.get("TOPICS_LOADER_TYPE", "FS")
        self.__loader: Loader = self.__loaders_factory(loader_type)
        self.__topics_metadata: list[Topic] = self.__loader.metadata
        print("Metadata", self.__topics_metadata)

    @property
    def topics_metadata(self) -> list[Topic]:
        return self.__topics_metadata

    def __loaders_factory(self, type: str) -> Loader:
        """"""
        if type == "FS":
            return FsLoader()
        return Loader("BASE")
