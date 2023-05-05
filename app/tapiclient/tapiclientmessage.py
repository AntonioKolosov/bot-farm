"""
"""

from typing import Dict

from .tapiclientutils import make_url, request_post
from .tapiclientconfig import cfg


async def send_a_message(message: Dict) -> bool:
    url = make_url(cfg.bot_url, 'sendMessage')
    resp = await request_post(url, message)
    return resp.status_code == 200
