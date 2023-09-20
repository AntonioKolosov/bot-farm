'''
'''

import os

from .loader import Loader
from .fsloader import FsLoader

from . import LOADER_BASE, LOADER_FS


class LoaderFactory:
    """"
    """
    def __init__(self) -> None:
        self.__loader_type = os.environ.get("TOPICS_LOADER_TYPE", LOADER_BASE)

    @property
    def loader_type(self) -> str:
        return self.__loader_type

    def loader(self) -> Loader:
        if self.loader_type == LOADER_FS:
            return FsLoader()
        return Loader(LOADER_BASE)
