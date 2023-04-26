from typing import Dict
from fastapi import APIRouter

# from ..schemas.tbdata import TBData
from ..tbotapi.tbotapiconfig import TbotAPIConfig


router = APIRouter()

tb_api = TbotAPIConfig()


@router.post("/hook", tags=["HOOK"])
async def message(data: Dict):
    ''''''

    #  Temporary - immediately send echo message
    chat_id = data['message']['chat']['id']
    text = data["message"]['text']
    message = {
        "text": text,
        "chat_id": chat_id,
    }

    res = await tb_api.send_a_message(message)

    return {"result": res}

# @router.post("/hook", tags=["HOOK"])
# async def message(data: TBData):
#     chat_id = data.message.chat.id
#     text = data.message.text
#     message = {
#             "text": text,
#             "chat_id": chat_id,
#         }

#     res = await tb_api.send_a_message(message)
#     return {"message": res}
