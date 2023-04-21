"""
"""


import os

from dotenv import load_dotenv
import urllib.parse as parse
import httpx


class RegisterWebhook:
    """"""

    def __init__(self):
        """"""
        load_dotenv()
        token = os.environ.get("BOT_TOKEN")
        bot_url = os.environ.get("BOT_URL")
        api_url = os.environ.get("API_URL")
        self.__token = token if token else ""
        self.__bot_url = bot_url if bot_url else ""
        self.__api_url = api_url if api_url else ""

    def set_webhook(self) -> None:
        """"""
        url = self.__make_url("setWebhook")
        httpx.get(url)
        return

    def unset_webhook(self) -> None:
        """"""
        url = self.__make_url("deleteWebhook")
        httpx.get(url)
        return

    def __make_url(self, method: str) -> str:
        """Make url for connection with bot"""
        params = {"url": self.__api_url}
        url = self.__bot_url.format(key=self.__token, method=method)
        if params:
            url = f'{url}?{parse.urlencode(params)}'
        return url
