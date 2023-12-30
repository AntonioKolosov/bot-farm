"""
'List' of avaible Services (TG, IG in future and so on)
"""


from src.data_def.schemas.answeringdata import AnsweringData
from .service import Service
from .tgservice.tgservice import TgService
from ..config import cfg


class ServicesList:
    """List of all exists services"""
    def __init__(self) -> None:
        self.__bot_types_list = cfg.bot_types_list
        self.__default_service = Service()
        self.__services: dict[str, Service] = {}
        for bt in self.__bot_types_list:
            self.__services[bt] = self.__service_factory(bt)

    def __service_factory(self, type: str) -> Service:
        """Create Startup objects regarding bot type"""
        if type == "TG":
            return TgService()
        return Service()

    def __get_service_by_type(self, type: str) -> Service:
        """Choose right service by type"""
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

    async def set_description(self,
                              service_type: str,
                              service_id: str,
                              descr: str) -> bool:
        """Set description"""
        service = self.__get_service_by_type(service_type)
        return await service.set_description(service_id, descr)

    async def set_keyboard_button(self,
                                  service_type: str,
                                  service_id: str,
                                  arr_arr_buttons) -> bool:
        """Set keyboard button"""
        service = self.__get_service_by_type(service_type)
        return await service.set_keyboard_button(service_id, arr_arr_buttons)
