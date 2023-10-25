'''
'''


from ..config import cfg
from .loader import Loader
from .fsloader import FsLoader

from .constants import LOADER_BASE, LOADER_FS


class LoaderFactory:
    """"
    """
    def __init__(self) -> None:
        self.__loader_type = cfg.loader_type
        print('LoaderFactory', self.__loader_type)

    @property
    def loader_type(self) -> str:
        return self.__loader_type

    def loader(self) -> Loader:
        if self.loader_type == LOADER_FS:
            return FsLoader(LOADER_FS)
        return Loader(LOADER_BASE)