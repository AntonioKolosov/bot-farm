"""
Loader Factory choose right loader
"""


from ..config import cfg
from .loader import Loader
from .mongoloader import MongoLoader

from .constants import LOADER_BASE, LOADER_MONGO


class LoaderFactory:
    """
    Choose right loader
    """
    def __init__(self) -> None:
        self.__loader_type = cfg.loader_type
        print('LoaderFactory', self.__loader_type)

    @property
    def loader_type(self) -> str:
        return self.__loader_type

    def loader(self) -> Loader:
        if self.loader_type == LOADER_MONGO:
            return MongoLoader(LOADER_MONGO)
        return Loader(LOADER_BASE)
