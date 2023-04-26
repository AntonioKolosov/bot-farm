"""
"""


import os
from typing import Dict, Union

import urllib.parse as parse
from httpx import AsyncClient, Response


class TbotAPIConfig:
    """"""

    def __init__(self):
        """"""
        token = os.environ.get("BOT_TOKEN")
        bot_url = os.environ.get("BOT_URL")
        api_url = os.environ.get("API_URL")
        self.__token = token if token else ""
        self.__bot_url = bot_url if bot_url else ""
        self.__api_url = f'{api_url}/hook' if api_url else ""

    async def set_webhook(self) -> bool:
        """"""
        params = {"url": self.__api_url}
        url = self.__make_url("setWebhook", params)
        resp = await self.__request_get(url)
        return resp.status_code == 200

    async def unset_webhook(self) -> bool:
        """"""
        url = self.__make_url("deleteWebhook")
        resp = await self.__request_get(url)
        return resp.status_code == 200

    async def send_a_message(self, message: Dict) -> bool:
        url = self.__make_url('sendMessage')
        resp = await self.__request_post(url, message)
        return resp.status_code == 200

    def __make_url(self, method: str,
                   params: Union[Dict, None] = None) -> str:
        """Make url for connection with bot"""
        url = self.__bot_url.format(key=self.__token, method=method)
        if params:
            url = f'{url}?{parse.urlencode(params)}'
        return url

    async def __request_get(self, url: str) -> Response:
        ''''''
        async with AsyncClient() as client:
            resp = await client.get(url)
            return resp

    async def __request_post(self, url: str, payload: dict) -> Response:
        ''''''
        async with AsyncClient() as client:
            resp = await client.post(url, json=payload)
            return resp
