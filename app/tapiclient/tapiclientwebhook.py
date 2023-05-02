"""
"""


from .tapiclientutils import make_url, request_get
from .tapiclientconfig import cfg


class TbotAPIWebhook:
    def __init__(self):
        """"""

    async def set_webhook(self) -> bool:
        """"""
        params = {"url": cfg.api_url}
        url = make_url(cfg.bot_url, "setWebhook", params)
        resp = await request_get(url)
        return resp.status_code == 200

    async def unset_webhook(self) -> bool:
        """"""
        url = make_url(cfg.bot_url, "deleteWebhook")
        resp = await request_get(url)
        return resp.status_code == 200
