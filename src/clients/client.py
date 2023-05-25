'''Base class for clients'''


from urllib import parse

from httpx import AsyncClient, Response


class Client:
    def __init__(self) -> None:
        pass

    def __make_url(self,
                   bot_url: str,
                   method: str,
                   params: dict | None = None) -> str:
        """Make url for connection with bot"""
        url = bot_url.format(method=method)
        if params:
            url = f'{url}?{parse.urlencode(params)}'
        return url

    async def __request_get(self, url: str) -> Response:
        ''''''
        async with AsyncClient() as client:
            resp = await client.get(url)
            return resp

    async def __request_post(self, url: str, payload: dict) -> Response:
        ''''''
        async with AsyncClient() as client:
            resp = await client.post(url, json=payload)
            return resp

    async def send_message(self, mess: dict) -> bool:
        ''''''
        return True
