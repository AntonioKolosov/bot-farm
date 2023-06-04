"""
"""


from .tgclientutils import make_url, request_get
from .tgclientconfig import cfg


async def set_webhook(bot_id: int) -> bool:
    """"""
    api_url = f'{cfg.api_url}/{bot_id}'
    params = {"url": api_url}
    url = make_url(cfg.bot_url, "setWebhook", params)
    resp = await request_get(url)
    return resp.status_code == 200


async def unset_webhook() -> bool:
    """"""
    url = make_url(cfg.bot_url, "deleteWebhook")
    resp = await request_get(url)
    return resp.status_code == 200
