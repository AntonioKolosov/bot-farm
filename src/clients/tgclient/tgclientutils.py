"""
"""

from typing import Union, Dict

import urllib.parse as parse
from httpx import AsyncClient, Response
from src.gtw.internals.tbotlogger import tb_log


def make_url(bot_url: str, method: str,
             params: Union[Dict, None] = None) -> str:
    """Make url for connection with bot"""
    url = bot_url.format(method=method)
    if params:
        url = f'{url}?{parse.urlencode(params)}'
    tb_log.log_info(f"{url}")
    return url


async def request_get(url: str) -> Response:
    ''''''
    async with AsyncClient() as client:
        resp = await client.get(url)
        tb_log.log_info(f"{resp.content}")
        return resp


async def request_post(url: str, payload: dict) -> Response:
    ''''''
    async with AsyncClient() as client:
        resp = await client.post(url, json=payload)
        tb_log.log_info(f"{resp.content}")
        return resp
