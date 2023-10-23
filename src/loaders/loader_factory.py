'''
'''

import os

from .loader import Loader
from .fsloader import FsLoader

from .constants import LOADER_BASE, LOADER_FS, TOPICS_LOADER_TYPE


class LoaderFactory:
    """"
    """
    def __init__(self) -> None:
        self.__loader_type = os.environ.get(TOPICS_LOADER_TYPE, LOADER_BASE)

    @property
    def loader_type(self) -> str:
        return self.__loader_type

    def loader(self) -> Loader:
        if self.loader_type == LOADER_FS:
            return FsLoader(LOADER_FS)
        return Loader(LOADER_BASE)
