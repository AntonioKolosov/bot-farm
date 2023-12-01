"""
"""

from abc import abstractmethod
from src.data_def.schemas.answeringdata import AnsweringData
from src.data_def.schemas.service_md import ServiceMetadata
from src.loaders import loader


class Service:
    """Base servise"""
    def __init__(self, type: str = "") -> None:
        self._service_type = type
        self._breaf_topics: list[dict[str, str]] = []
        self._bots_id_2_names: list = []
        self._service_metadata: dict[str, ServiceMetadata] = {}
        if type != '':
            self.__load_metadata()

    def _get_alias_by_id(self, service_alias: str) -> str:
        """"""
        for id_2_name in self._bots_id_2_names:
            id, name = id_2_name.split(":")
            if id == service_alias:
                return name
        return "default"

    def _get_id_by_alias(self, service_alias: str) -> str:
        """"""
        for id_2_name in self._bots_id_2_names:
            id, name = id_2_name.split(":")
            if name == service_alias:
                return id
        return ""

    def __load_metadata(self):
        ''''''
        names = loader.load_names()
        for name in names:
            metadata = loader.load_metadata(name)
            srv_metadata = ServiceMetadata(**metadata)
            if srv_metadata.service_type == self._service_type:
                key = srv_metadata.service_alias
                self._service_metadata[key] = srv_metadata

    @abstractmethod
    async def startup(self) -> None:
        """"""

    @abstractmethod
    async def shutdown(self) -> None:
        """"""

    @abstractmethod
    def __endpoint_for_request(self,
                               bot_id: str,
                               method: str,
                               params: dict | None = None) -> str:
        """"""

    @abstractmethod
    async def send_message(self, answer: AnsweringData) -> bool:
        """"""

    @abstractmethod
    def __make_endpoints(self) -> None:
        """Instantiate enpoints"""
