"""
"""


import os

from src.internals import utilites
from src.proc_data.schemas.answeringdata import AnsweringData
from ..service import Service
from .tgapi import send_message
from .tgapi import set_webhook, delete_webhook
from .tgapi import delete_commands, set_command, get_commands
from .tgapi import get_chat_menu_button, set_chat_menu_button


class TgService(Service):
    """Telegram service"""
    def __init__(self) -> None:
        super().__init__("TG")
        self.__endpoint_template = "https://api.telegram.org/bot{key}/{method}"
        tokens = os.environ.get("TG_BOTS_TOKENS", "[\"error:error\"]")
        self.__tokens = list(map(str, tokens[1:-1].split(",")))
        self.__gtw_url = os.environ.get("GTW_URL", "")
        bots_id_2_names = os.environ.get("TG_BOTS_ID_2_NAMES",
                                         "[\"error:error\"]")
        self._bots_id_2_names = list(map(str,
                                         bots_id_2_names[1:-1].split(",")))
        self.__endpoints: dict[str, str] = {}
        self.__make_endpoints()

    async def send_message(self, answer: AnsweringData) -> bool:
        """Wrapper for API"""
        bot_id = self._get_id_by_alias(answer.service_alias)
        endpoint = self.__endpoints.get(bot_id, "")
        tg_answer = utilites.tg_answer_converter(bot_id, answer)
        return await send_message(endpoint, tg_answer)

    async def startup(self) -> None:
        """"""
        for b_id, ep in self.__endpoints.items():
            await self.__initialize(b_id)

    async def shutdown(self) -> None:
        """"""
        for b_id, ep in self.__endpoints.items():
            await self.__close(b_id)

    async def __initialize(self, bot_id: str) -> None:
        """"""
        # convert bot_id to bot_name
        alias = self._get_alias_by_id(bot_id)
        # get endpoints names from topics
        endpoints_names = [{"name": topic.get("name", ""),
                            "descr": topic.get("descr", "")}
                           for topic in self._breaf_topics
                           if topic.get("service_alias") == alias]
        print(f"Initialize the {alias} endpoint")
        await self.__delete_menu_commands(bot_id)
        await self.__set_menu_commands(bot_id, endpoints_names)
        await self.__set_menu_button(bot_id, True)
        await self.__set_webhook(bot_id, alias)
        # for test
        await self.__get_menu_button(bot_id)
        await self.__get_menu_commands(bot_id)

    async def __close(self, bot_id: str) -> None:
        """"""
        alias = self._get_alias_by_id(bot_id)
        print(f"CLose the {alias} endpoint")
        await self.__delete_webhook(bot_id)
        await self.__delete_menu_commands(bot_id)
        await self.__set_menu_button(bot_id)
        # for test
        await self.__get_menu_button(bot_id)
        await self.__get_menu_commands(bot_id)

    async def __set_webhook(self, bot_id: str, alias: str) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        gtw_url = f"{self.__gtw_url}/tgincdata/{alias}"
        return await set_webhook(endpoint, gtw_url)

    async def __delete_webhook(self, bot_id: str) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await delete_webhook(endpoint)

    async def __delete_menu_commands(self, bot_id) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await delete_commands(endpoint)

    async def __get_menu_commands(self, bot_id) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await get_commands(endpoint)

    async def __set_menu_commands(self,
                                  bot_id: str,
                                  topics_names: list[dict[str, str]]) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        commands = list()
        for tn in topics_names:
            cmd = {
                "command": tn.get("name", ""),
                "description": tn.get("descr", "")
            }
            commands.append(cmd)
        return await set_command(endpoint, commands)

    async def __set_menu_button(self, bot_id: str, cmd: bool = False) -> bool:
        """Wrapper for API"""
        button = {"type": "default"}
        if cmd:
            button = {"type": "commands"}
        endpoint = self.__endpoints.get(bot_id, "")
        return await set_chat_menu_button(endpoint, button)

    async def __get_menu_button(self, bot_id: str) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await get_chat_menu_button(endpoint)

    def __make_endpoints(self) -> None:
        """Instantiate enpoints"""
        for t in self.__tokens:
            bot_id, _ = t.split(":")
            
            endpoint = self.__set_token_to_endpoint(t)
            self.__endpoints[bot_id] = endpoint

    def __set_token_to_endpoint(self, token: str) -> str:
        """Set token for an endpoint"""
        return self.__endpoint_template.format(key=token, method="{method}")
