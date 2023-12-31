"""
Send messages to chats, bots
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
        """Get alias for choosing bot"""
        for id_2_name in self._bots_id_2_names:
            id, name = id_2_name.split(":")
            if id == service_alias:
                return name
        return "default"

    def _get_id_by_alias(self, service_alias: str) -> str:
        """Get id for choosing chat"""
        for id_2_name in self._bots_id_2_names:
            id, name = id_2_name.split(":")
            if name == service_alias:
                return id
        return ""

    def __load_metadata(self):
        """Load metadata"""
        names = loader.load_names()
        for name in names:
            metadata = loader.load_metadata(name)
            srv_metadata = ServiceMetadata(**metadata)
            if srv_metadata.service_type == self._service_type:
                key = srv_metadata.service_alias
                self._service_metadata[key] = srv_metadata

    @abstractmethod
    async def startup(self) -> None:
        """Startup service"""

    @abstractmethod
    async def shutdown(self) -> None:
        """Shutdown service"""

    @abstractmethod
    def __endpoint_for_request(self,
                               bot_id: str,
                               method: str,
                               params: dict | None = None) -> str:
        """Make right endpoint"""

    @abstractmethod
    async def send_message(self, answer: AnsweringData) -> bool:
        """Send message to chats, bots"""

    @abstractmethod
    def __make_endpoints(self) -> None:
        """Instantiate enpoints"""

    @abstractmethod
    async def set_description(self,
                              service_id: str,
                              descr: str) -> bool:
        """Set description"""

    # @abstractmethod
    # async def set_menu(self,
    #                    service_id: str) -> bool:
    #     """Set menu button"""

    # @abstractmethod
    # async def set_keyboard_button(self,
    #                               service_id: str) -> bool:
    #     """Set keyboard button"""

    @abstractmethod
    async def set_buttons(self, answer: AnsweringData) -> bool:
        """Send message to chats, bots"""
