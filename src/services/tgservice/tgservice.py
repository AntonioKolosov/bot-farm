"""
"""


import json
import os
from urllib import parse

from ..service import Service
from ..requests import request_get, request_post
from src.gtw.internals.tbotlogger import tb_log


class TgService(Service):
    """Telegram service"""
    def __init__(self) -> None:
        super().__init__("TG")
        self.__endpoint_template = os.environ.get("TG_BOTS_URL", "error")
        tokens = os.environ.get("TG_BOTS_TOKENS", "[\"error:error\"]")
        self.__tokens = list(map(str, tokens[1:-1].split(",")))
        self.__gtw_url = os.environ.get("GTW_URL")
        self.__endpoints: dict[str, str] = {}
        self.__make_endpoints()

    async def startup(self, topics_names: list[dict[str, str]]) -> None:
        """"""
        print(f"Initialize all {self.__doc__} endpoints")
        for b_id, ep in self.__endpoints.items():
            await self.__initialize(b_id, topics_names)

    async def shutdown(self) -> None:
        """"""
        print(f"Shutdown {self.__doc__} and close all its endpoints")
        for b_id, ep in self.__endpoints.items():
            await self.__close(b_id)

    async def send_message(self, service_id: str, answer: dict) -> bool:
        """"""
        endpoint = self.__endpoint_for_request(service_id, "sendMessage")
        resp = await request_post(endpoint, answer)
        return resp.status_code == 200

    async def __initialize(self,
                           bot_id: str,
                           topics_names: list[dict[str, str]]) -> None:
        """"""
        print(f"Initialize the {bot_id} endpoint")
        await self.__clean(bot_id)
        await self.__set_menu_commands(bot_id, topics_names)
        await self.__set_webhook(bot_id)

    async def __close(self, bot_id: str) -> None:
        """"""
        print(f"CLose the {bot_id} endpoint")
        await self.__delete_webhook(bot_id)
        await self.__clean(bot_id)

    async def __clean(self, bot_id) -> bool:
        """Delete menu commands"""
        endpoint = self.__endpoint_for_request(bot_id, "deleteMyCommands")
        resp = await request_get(endpoint)
        tb_log.log_info(f"{resp.content}")
        return resp.status_code == 200

    async def __set_menu_commands(self,
                                  bot_id: str,
                                  topics_names: list[dict[str, str]]) -> None:
        """"""
        commands = topics_names
        cmd_list = list()
        for c in commands:
            cmd = {
                "command": c.get("name"),
                "description": c.get("descr")
            }
            cmd_list.append(cmd)
        await self.__set_commands(bot_id, cmd_list)

    async def __set_commands(self,
                             bot_id: str,
                             commands: list[dict[str, str]]) -> bool:
        """"""
        params = {"commands": json.dumps(commands)}
        endpoint = self.__endpoint_for_request(bot_id, "setMyCommands", params)
        resp = await request_get(endpoint)
        return resp.status_code == 200

    async def __set_webhook(self, bot_id: str) -> bool:
        """"""
        gtw_url = f"{self.__gtw_url}/tgincdata/{bot_id}"
        params = {"url": gtw_url}
        endpoint = self.__endpoint_for_request(bot_id, "setWebhook", params)
        resp = await request_get(endpoint)
        tb_log.log_info(f"{resp.content}")
        return resp.status_code == 200

    async def __delete_webhook(self, bot_id: str) -> bool:
        """"""
        endpoint = self.__endpoint_for_request(bot_id, "deleteWebhook")
        resp = await request_get(endpoint)
        tb_log.log_info(f"{resp.content}")
        return resp.status_code == 200

    def __endpoint_for_request(self,
                               bot_id: str,
                               method: str,
                               params: dict | None = None) -> str:
        """Make endpoint url for connection with a bot"""
        endpoint = self.__endpoints.get(bot_id, "{method}")
        endpoint = endpoint.format(method=method)
        if params:
            endpoint = f'{endpoint}?{parse.urlencode(params)}'
        tb_log.log_info(f"{endpoint}")
        return endpoint

    def __make_endpoints(self) -> None:
        """Instantiate enpoints"""
        for t in self.__tokens:
            bot_id, _ = t.split(":")
            endpoint = self.__get_endpoint(t)
            self.__endpoints[bot_id] = endpoint

    def __get_endpoint(self, token: str) -> str:
        """"""
        return self.__endpoint_template.format(key=token, method="{method}")
