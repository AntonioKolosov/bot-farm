"""
Descripe Telegram Api for https://api.telegram.org/bot{key}/{method}
"""


import json
from urllib import parse

from ..requests import request_get, request_post
from src.internals.tbotlogger import tb_log


async def set_my_name(endpoint: str, name: str) -> bool:
    """Set a bot name"""
    params = {"name": name}
    endpoint4r = __endpoint_for_request(endpoint, "setMyName", params)
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def set_description(endpoint: str, descr: str) -> bool:
    """Set a description"""
    params = {"description": descr}
    endpoint4r = __endpoint_for_request(endpoint, "", params)
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def set_keyboard_button(endpoint: str, arr_arr_buttons) -> bool:
    """Set a keyboard button"""
    params = arr_arr_buttons
    endpoint4r = __endpoint_for_request(endpoint,
                                        "sendMessage",
                                        params)
    print(endpoint4r)
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def send_message(endpoint: str, answer: dict) -> bool:
    """Send a message to an endpoint"""
    endpoint4r = __endpoint_for_request(endpoint, "sendMessage")
    resp = await request_post(endpoint4r, answer)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def set_webhook(endpoint: str, gtw_url: str) -> bool:
    """Set webhook for an endpoint"""
    params = {"url": gtw_url}
    endpoint4r = __endpoint_for_request(endpoint, "setWebhook", params)
    tb_log.log_info(endpoint4r)
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def delete_webhook(endpoint: str) -> bool:
    """Delete webhook from an endpoint"""
    endpoint4r = __endpoint_for_request(endpoint, "deleteWebhook")
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def set_command(endpoint: str,
                      command: list[dict[str, str]]) -> bool:
    """Set commands to bot"""
    # Lie menu
    params = {"commands": json.dumps(command)}
    endpoint4r = __endpoint_for_request(endpoint,
                                        "setMyCommands",
                                        params)
    tb_log.log_info(f"{endpoint4r}")
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def delete_commands(endpoint: str) -> bool:
    """Delete menu commands"""
    endpoint4r = __endpoint_for_request(endpoint, "deleteMyCommands")
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def get_commands(endpoint: str) -> bool:
    """Get menu commands"""
    endpoint4r = __endpoint_for_request(endpoint, "getMyCommands")
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def set_chat_menu_button(endpoint: str, button: dict) -> bool:
    """Change the bot's menu button in
    a private chat, or the default menu button"""
    # Like web
    # params = { "menu_button":
    # {"type": "web_app", "text": "github", "web_app":
    # {"url": "https://github.com"}}} # works!!!
    # Lie buttons
    # params = {"menu_button": json.dumps(command)}
    params = {"menu_button": json.dumps(button)}
    endpoint4r = __endpoint_for_request(endpoint, "setChatMenuButton", params)
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


async def get_chat_menu_button(endpoint: str) -> bool:
    """Set a bot name"""
    endpoint4r = __endpoint_for_request(endpoint, "getChatMenuButton")
    resp = await request_get(endpoint4r)
    tb_log.log_info(f"{resp.content}")
    return resp.status_code == 200


def __endpoint_for_request(endpoint: str,
                           method: str,
                           params: dict | None = None) -> str:
    """Make endpoint url for connection with a bot"""
    endpoint4r = endpoint.format(method=method)
    if params:
        endpoint4r = f'{endpoint4r}?{parse.urlencode(params)}'
    return endpoint4r
