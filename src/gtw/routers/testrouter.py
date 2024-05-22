"""
Test router. You may use it for tests with API
"""


from typing import List
from fastapi import APIRouter

# Websocket
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

from src.services import services


router = APIRouter()


@router.post("/descr", tags=["TEST"])
async def set_description_req():
    """This method sets descriprion"""
    description = "Hello, I'm new Bot!!!!!!!!!!!!!!!"
    bot_id = "6049337649"
    res = await services.set_description('TG', bot_id, description)
    print(res)
    return {"Descr": f"Set {res}"}


@router.get("/webdata/{lang}")
async def getweb_data(lang):
    filename = f'{lang}_data.json'
    filepath = f"./static/webdata/{filename}"
    return FileResponse(filepath)


class Notifier:
    def __init__(self):
        self.connections: List[WebSocket] = []
        self.generator = self.get_notification_generator()

    async def get_notification_generator(self):
        while True:
            message = yield
            await self._notify(message)

    async def push(self, msg: str):
        await self.generator.asend(msg)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def remove(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def _notify(self, message: str):
        living_connections = []
        while len(self.connections) > 0:
            # Looping like this is necessary
            # in case a disconnection is handled
            # during await websocket.send_text(message)
            websocket = self.connections.pop()
            await websocket.send_text(message)
            living_connections.append(websocket)
        self.connections = living_connections


notifier = Notifier()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await notifier.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        notifier.remove(websocket)


@router.get("/push/{message}")
async def push_to_connected_websockets(message: str):
    await notifier.push(message)
