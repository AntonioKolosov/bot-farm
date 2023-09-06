"""
"""

from abc import abstractmethod
from src.proc_data.schemas.answeringdata import AnsweringData


class Service:
    """Base servise"""
    def __init__(self, type: str = "") -> None:
        self._service_type = type
        self._breaf_topics: list[dict[str, str]] = []
        self._bots_id_2_names: list = []

    def _get_alias_by_id(self, service_id: str) -> str:
        """"""
        for id_2_name in self._bots_id_2_names:
            id, name = id_2_name.split(":")
            if id == service_id:
                return name
        return "default"

    def _get_id_by_alias(self, service_alias: str) -> str:
        """"""
        for id_2_name in self._bots_id_2_names:
            id, name = id_2_name.split(":")
            if name == service_alias:
                return id
        return ""

    def add_breaf(self, topic: dict[str, str]) -> None:
        """"""
        self._breaf_topics.append(topic)

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
