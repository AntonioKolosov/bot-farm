import json
from fastapi import APIRouter

# from ..schemas.tbdata import TBDat
from src.services import services


router = APIRouter()


@router.post("/descr", tags=["TEST"])
async def set_description_req():
    """"""
    description = "Hello, I'm new Bot!!!!!!!!!!!!!!!"
    bot_id = "6049337649"
    res = await services.set_description('TG', bot_id, description)
    print(res)
    return {"Descr": f"Set {res}"}


@router.post("/button", tags=["TEST"])
async def set_keyboard_button():
    """"""
#     keyboard = [
#     [{"text": "Button 1", "callback_data": "1"}]
# ]

    keyboard = {
        "keyboard": [[{"text": "/info"}]],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }
    keyboard = json.dumps(keyboard)

    arr_arr_buttons = {
        "chat_id": 339914913,
        "text": "Info1234",
        "reply_markup": keyboard
    }
    bot_id = "6049337649"
    res = await services.set_keyboard_button('TG', bot_id, arr_arr_buttons)
    return {"Button:" f"Set {res}"}


# @router.post("/cmd", tags=["TEST"])
# async def set_commands():
#     """"""
#     cmd_list = [
#         {
#             "command": "help",
#             "description": "How to use this bot"
#         }
#     ]
#     res = await t_sp.set_commands(cmd_list)
#     return {"Commands": f"Set {res}"}

# @router.post("/del", tags=["ROOT"])
# async def delete_commands():
#     """"""
#     res = await t_sp.delete_commands()
#     return {"Commands": f"Deleted {res}"}
