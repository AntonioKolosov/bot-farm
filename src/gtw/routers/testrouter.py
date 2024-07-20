"""
Test router. You may use it for tests with API
"""


from typing import List
from fastapi import APIRouter

# Websocket
from fastapi import WebSocket, WebSocketDisconnect

from src.loaders import loader
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


# # https://url/prompter?page=index or https://url/prompter
# @router.get("/{app}")
# async def getweb_view(app, page: str = 'index'):
#     webview = loader.load_webview(app, 'views', page)
#     webview_orig = base64.b64decode(webview)
#     return HTMLResponse(content=webview_orig,
#                         media_type='text/html',
#                         status_code=200)


# # https://url/prompter?style=main or https://url/prompter
# @router.get("/webstyle/{app}")
# async def getweb_style(app, style: str = 'main'):
#     webstyle = loader.load_style(app, 'styles', style)
#     webstyle_orig = base64.b64decode(webstyle)
#     return HTMLResponse(content=webstyle_orig,
#                         media_type='text/css',
#                         status_code=200)


# @router.get("/webscript/{app}/{script}")
# async def getweb_script(app, script):
#     webscript = loader.load_script(app, 'scripts', script)
#     webscript_orig = base64.b64decode(webscript)
#     return HTMLResponse(content=webscript_orig,
#                         media_type='text/javascript',
#                         status_code=200)


@router.get("/webdata/{lang}")
async def getweb_data(lang):
    # filename = f'{lang}_data.json'
    # from static
    # filepath = f"./static/webdata/{filename}"
    # return FileResponse(filepath)
    # from DB
    doc_name = f'{lang}_data'
    content = loader.load_content(doc_name)
    if type(content) == dict:
        content_value = content['content']
    elif type(content) == str:
        content_value = content
    return {"content": content_value}


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
