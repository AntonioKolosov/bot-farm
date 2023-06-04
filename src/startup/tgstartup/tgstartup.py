"""
TG Startup module
"""


import json
import os

from src.startup.startup import Startup
from src.clients.tgclient import tgclientsetup as t_sp
from src.clients.tgclient import tgclientwebhook as t_wh
from src.messanger.mess_dispatcher import dsp


class TgStartup(Startup):
    def __init__(self) -> None:
        """"""
        super().__init__(type="TG")
        self.__tokens = json.loads(
            os.environ.get("TG_BOTS_TOKENS", "[\"\"]")
        )
        self.__url = os.environ.get("TG_BOTS_URL", "")

    async def startup(self):
        """"""
        # Clean UI
        await self.__clean()
        # Set commands menu
        await self.__set_menu_commands()
        # Set webhook
        await self.__set_webhook()

    async def shutdown(self):
        """"""
        await t_wh.unset_webhook()
        await self.__clean()

    async def __clean(self):
        """"""
        await t_sp.delete_commands()

    async def __set_menu_commands(self):
        """"""
        commands = dsp.topics_names()
        cmd_list = []
        for c in commands:
            cmd = {
                "command": c.get("name"),
                "description": c.get("descr")
            }
            cmd_list.append(cmd)
        await t_sp.set_commands(cmd_list)

    async def __set_webhook(self):
        """"""
        await t_wh.set_webhook()
