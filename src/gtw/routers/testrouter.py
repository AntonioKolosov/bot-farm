"""
Test router. You may use it for tests with API
"""


import json
from fastapi import APIRouter

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


@router.post("/button", tags=["TEST"])
async def set_keyboard_button():
    """This methods sets keyboard button"""
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
