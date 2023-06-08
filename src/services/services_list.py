"""

"""


import os
from .service import Service
from .tgservice.tgservice import TgService


class ServicesList:
    """List of all exists services"""
    def __init__(self) -> None:
        """"""
        # self.__bot_types_list = list()
        bot_types = os.environ.get("BOT_TYPES_LIST", "[\"error:error\"]")
        self.__bot_types_list = list(map(str, bot_types[1:-1].split(",")))

        self.__topics_names: list[dict[str, str]] = list()
        self.__default_service = Service()
        self.__services: dict[str, Service] = {}
        for bt in self.__bot_types_list:
            self.__services[bt] = self.__service_factory(bt)

    def set_topics_names(self, topics_names) -> None:
        """"""
        self.__topics_names = topics_names

    def __service_factory(self, type: str) -> Service:
        """Create Startup objects regarding bot type"""
        if type == "TG":
            return TgService()
        return Service()

    def __get_service_by_type(self, type: str) -> Service:
        """"""
        return self.__services.get(type, self.__default_service)

    async def startup(self) -> None:
        """Start up all exists services"""
        for t, s in self.__services.items():
            await s.startup(self.__topics_names)

    async def shutdown(self) -> None:
        """Shutdown all exists services"""
        for t, s in self.__services.items():
            await s.shutdown()

    async def send_message(self,
                           service_type: str,
                           service_id: str,
                           answer: dict):
        """Send message to the corresponding service"""
        service = self.__get_service_by_type(service_type)
        await service.send_message(service_id, answer)