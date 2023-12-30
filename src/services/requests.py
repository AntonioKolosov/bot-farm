"""
Requests
"""


from httpx import AsyncClient, Response


async def request_get(url: str) -> Response:
    """GET request"""
    async with AsyncClient() as client:
        resp = await client.get(url)
        return resp


async def request_post(url: str, payload: dict) -> Response:
    """POST request"""
    async with AsyncClient() as client:
        resp = await client.post(url, json=payload)
        return resp
