"""
"""

import json
from .tapiclientutils import make_url, request_get
from .tapiclientconfig import cfg


async def set_description(descr: str) -> bool:
    """"""
    params = {"description": descr}
    url = make_url(cfg.bot_url, "setMyDescription", params)
    resp = await request_get(url)
    return resp.status_code == 200


async def set_commands(commands: list) -> bool:
    """"""
    params = {"commands": json.dumps(commands)}
    url = make_url(cfg.bot_url, "setMyCommands", params)
    resp = await request_get(url)
    return resp.status_code == 200


async def delete_commands() -> bool:
    """"""
    url = make_url(cfg.bot_url, "deleteMyCommands")
    resp = await request_get(url)
    return resp.status_code == 200
