"""
"""


import os

from ..service import Service
from .tgapi import send_message
from .tgapi import set_webhook, delete_webhook
from .tgapi import delete_commands, set_command, get_commands
from .tgapi import get_chat_menu_button, set_chat_menu_button


class TgService(Service):
    """Telegram service"""
    def __init__(self) -> None:
        super().__init__("TG")
        self.__endpoint_template = os.environ.get("TG_BOTS_URL", "error")
        tokens = os.environ.get("TG_BOTS_TOKENS", "[\"error:error\"]")
        self.__tokens = list(map(str, tokens[1:-1].split(",")))
        self.__gtw_url = os.environ.get("GTW_URL", "")
        bots_id_2_names = os.environ.get("TG_BOTS_ID_2_NAMES",
                                         "[\"error:error\"]")
        self._bots_id_2_names = list(map(str,
                                         bots_id_2_names[1:-1].split(",")))
        self.__endpoints: dict[str, str] = {}
        self.__make_endpoints()

    async def send_message(self, bot_id: str, answer: dict) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await send_message(endpoint, answer)

    async def startup(self) -> None:
        """"""
        print(f"Initialize all {self.__doc__} endpoints")
        for b_id, ep in self.__endpoints.items():
            await self.__initialize(b_id)

    async def shutdown(self) -> None:
        """"""
        print(f"Shutdown {self.__doc__} and close all its endpoints")
        for b_id, ep in self.__endpoints.items():
            await self.__close(b_id)

    async def __initialize(self, bot_id: str) -> None:
        """"""
        # convert bot_id to bot_name
        bot_name = self.get_alias(bot_id)
        # get endpoints names from topics
        endpoints_names = [{"name": topic.get("name", ""),
                            "descr": topic.get("descr", "")}
                           for topic in self._breaf_topics
                           if topic.get("service_id") == bot_name]
        print(f"Initialize the {bot_id} endpoint")
        await self.__delete_menu_commands(bot_id)
        await self.__set_menu_commands(bot_id, endpoints_names)
        await self.__set_menu_button(bot_id, True)
        await self.__set_webhook(bot_id)
        # for test
        await self.__get_menu_button(bot_id)
        await self.__get_menu_commands(bot_id)

    async def __close(self, bot_id: str) -> None:
        """"""
        print(f"CLose the {bot_id} endpoint")
        await self.__delete_webhook(bot_id)
        await self.__delete_menu_commands(bot_id)
        await self.__set_menu_button(bot_id)
        # for test
        await self.__get_menu_button(bot_id)
        await self.__get_menu_commands(bot_id)

    async def __set_webhook(self, bot_id: str) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        gtw_url = f"{self.__gtw_url}/tgincdata/{bot_id}"
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
