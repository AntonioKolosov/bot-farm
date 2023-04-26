"""
"""


import os
from typing import Dict

from .tbotapiutils import make_url, request_get, request_post


class TbotAPIConfig:
    """"""

    def __init__(self):
        """"""
        token = os.environ.get("BOT_TOKEN")
        bot_url = os.environ.get("BOT_URL")
        api_url = os.environ.get("API_URL")
        token = token if token else ""
        self.__bot_url = bot_url if bot_url else ""
        self.__bot_url = self.__bot_url.format(key=token, method="")
        self.__api_url = f'{api_url}/hook' if api_url else ""

    async def set_webhook(self) -> bool:
        """"""
        params = {"url": self.__api_url}
        url = make_url(self.__bot_url, "setWebhook", params)
        resp = await request_get(url)
        return resp.status_code == 200

    async def unset_webhook(self) -> bool:
        """"""
        url = make_url(self.__bot_url, "deleteWebhook")
        resp = await request_get(url)
        return resp.status_code == 200

    async def send_a_message(self, message: Dict) -> bool:
        url = make_url(self.__bot_url, 'sendMessage')
        resp = await request_post(url, message)
        return resp.status_code == 200
