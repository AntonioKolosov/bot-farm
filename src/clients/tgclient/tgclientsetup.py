"""
"""

import json
from .tgclientutils import make_url, request_get, request_post
from .tgclientconfig import cfg


async def set_my_name(name: str) -> bool:
    """
    The method to change the bot's description, which is
    shown in the chat with the bot if the chat is empty.
    """
    params = {"name": name}
    url = make_url(cfg.bot_url, "setMyName", params)
    resp = await request_get(url)
    return resp.status_code == 200


async def set_description(descr: str) -> bool:
    """"""
    params = {"description": descr}
    url = make_url(cfg.bot_url, "setMyDescription", params)
    resp = await request_get(url)
    return resp.status_code == 200


async def set_commands(commands: list[dict[str, str]]) -> bool:
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


# Menu Buttons
async def set_chat_menu_button(button: dict):
    """
    The method to change the bot's menu button in
    a private chat, or the default menu button
    """
    params = {"menu_button": json.dumps(button)}
    url = make_url(cfg.bot_url, "setChatMenuButton", params)
    resp = await request_get(url)
    return resp.status_code == 200


async def message_with_keyboard(message: dict):
    """"""
    url = make_url(cfg.bot_url, 'sendMessage')
    resp = await request_post(url, message)
    return resp.status_code == 200
