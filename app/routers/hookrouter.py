from typing import Dict
from fastapi import APIRouter

# from ..schemas.tbdata import TBData
from ..tbotapi.tbotapimessage import TbotAPIMessage
from ..internals.tbotlogger import tb_log


router = APIRouter()


tb_mess = TbotAPIMessage()


@router.post("/hook", tags=["HOOK"])
async def message(data: Dict):
    ''''''
    tb_log.log_info(f"{data}")
    # Temporary - immediately send echo message
    chat_id = data['message']['chat']['id']
    text = data["message"]['text']
    message = {
        "text": text,
        "chat_id": chat_id,
    }

    res = await tb_mess.send_a_message(message)

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