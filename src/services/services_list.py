"""

"""


import os

from src.proc_data.schemas.answeringdata import AnsweringData
from .service import Service
from .tgservice.tgservice import TgService


class ServicesList:
    """List of all exists services"""
    def __init__(self) -> None:
        """"""
        # self.__bot_types_list = list()
        bot_types = os.environ.get("BOT_TYPES_LIST", "[\"error:error\"]")
        self.__bot_types_list = list(map(str, bot_types[1:-1].split(",")))

        self.__default_service = Service()
        self.__services: dict[str, Service] = {}
        for bt in self.__bot_types_list:
            self.__services[bt] = self.__service_factory(bt)

    def set_breaf_topics(self, breaf_topics: list[dict[str, str]]) -> None:
        """"""
        for type, service in self.__services.items():
            for topic in breaf_topics:
                if type == topic.get("service_type"):
                    service.add_breaf(topic)

    def get_alias(self, type, id) -> str:
        service = self.__services.get(type, self.__default_service)
        return service.get_alias(id)

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
            await s.startup()

    async def shutdown(self) -> None:
        """Shutdown all exists services"""
        for t, s in self.__services.items():
            await s.shutdown()

    async def send_message(self, answer: AnsweringData):
        """Send message to the corresponding service"""
        service = self.__get_service_by_type(answer.service_type)
        await service.send_message(answer)
