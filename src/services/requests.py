"""
Requests
"""


from httpx import AsyncClient, Response


async def request_get(url: str) -> Response:
    ''''''
    async with AsyncClient() as client:
        resp = await client.get(url)
        return resp


async def request_post(url: str, payload: dict) -> Response:
    ''''''
    async with AsyncClient() as client:
        resp = await client.post(url, json=payload)
        return resp
