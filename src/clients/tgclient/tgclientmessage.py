"""
"""

from typing import Dict

from .tgclientutils import make_url, request_post
from .tgclientconfig import cfg


async def send_message(message: Dict) -> bool:
    url = make_url(cfg.bot_url, 'sendMessage')
    resp = await request_post(url, message)
    return resp.status_code == 200
