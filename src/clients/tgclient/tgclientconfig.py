"""
"""


import os


class TbotAPIConfig:
    """"""

    def __init__(self):
        """"""
        token = os.environ.get("BOT_TOKEN")
        bot_url = os.environ.get("BOT_URL")
        api_url = os.environ.get("API_URL")
        token = token if token else ""
        self.__bot_url = bot_url if bot_url else ""
        self.__bot_url = self.__bot_url.format(key=token, method="{method}")
        self.__api_url = f'{api_url}/tgdata' if api_url else ""

    @property
    def bot_url(self):
        return self.__bot_url

    @property
    def api_url(self):
        return self.__api_url


cfg = TbotAPIConfig()
