"""
"""

from fastapi import APIRouter

# from ..schemas.tbdata import TBData
from src.clients.tgclient import tgclientsetup as t_sp

router = APIRouter()


@router.post("/name", tags=["TEST"])
async def set_my_name():
    """"""
    name = "Ipsum Bot"
    res = await t_sp.set_my_name(name)
    return {"Name": f"Set {res}"}


@router.post("/descr", tags=["TEST"])
async def set_description():
    """"""
    description = "Hello, I'm new Bot"
    res = await t_sp.set_description(description)
    return {"Descr": f"Set {res}"}


@router.post("/cmd", tags=["TEST"])
async def set_commands():
    """"""
    cmd_list = [
        {
            "command": "help",
            "description": "How to use this bot"
        }
    ]
    res = await t_sp.set_commands(cmd_list)
    return {"Commands": f"Set {res}"}


@router.post("/del", tags=["TEST"])
async def delete_commands():
    """"""
    res = await t_sp.delete_commands()
    return {"Commands": f"Deleted {res}"}


@router.post("/mnbuttton", tags=["TEST"])
async def set_chat_menu_button():
    """"""
    # button = {"type": "web_app", "text": "github",
    # "web_app": {"url": "https://github.com"}} # works!!!
    button = {"type": "commands"}  # works too
    res = await t_sp.set_chat_menu_button(button)
    return {"menu button": f"Set {res}"}


@router.post("/setreplaykeyboard", tags=["TEST"])
async def set_reply_keyboard():
    """"""
    message = {
        "chat_id": 885886200,
        "text": "press the button",
        "reply_markup": {
            "keyboard": [[
                {
                    "text": "How do I report an issue?"
                }
            ]],
            "one_time_keyboard": True
        }
    }
    # "text will be sent to the bot"
    res = await t_sp.message_with_keyboard(message)
    return {"replay keyboard": f"Set {res}"}


# @router.post("/setinlinekeyboard", tags=["TEST"])
# async def set_inline_keyboard():
#     """"""
#     message = {
#         "chat_id": 885886200,
#         "text": "press the button",
#         "reply_markup": {
#             "inline_keyboard": [[
#                 {
#                     "text": "BA",
#                     "callback_data": "A1"
#                 },
#                 {
#                     "text": "BB",
#                     "callback_data": "C1"
#                 }]
#             ]
#         }
#     }
#     res = await t_sp.inline_keyboard(message)
#     return {"inline keyboard": f"Set {res}"}
