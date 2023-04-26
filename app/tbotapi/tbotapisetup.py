"""
"""

import json
from .tbotapiutils import make_url, request_get
from .tbotapiconfig import cfg


class TBotAPISetup:
    def __init__(self) -> None:
        """"""
        pass

    async def set_description(self, descr: str) -> bool:
        """"""
        params = {"description": descr}
        url = make_url(cfg.bot_url, "setMyDescription", params)
        resp = await request_get(url)
        return resp.status_code == 200

    async def set_commands(self, commands: list) -> bool:
        """"""
        params = {"commands": json.dumps(commands)}
        url = make_url(cfg.bot_url, "setMyCommands", params)
        resp = await request_get(url)
        return resp.status_code == 200

    async def delete_commands(self) -> bool:
        """"""
        url = make_url(cfg.bot_url, "deleteMyCommands")
        resp = await request_get(url)
        return resp.status_code == 200
