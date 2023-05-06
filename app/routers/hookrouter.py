from typing import Dict
from fastapi import APIRouter, BackgroundTasks

# from ..schemas.tbdata import TBData
from app.tapiclient.tapiclientmessage import send_message
from app.internals.tbotlogger import tb_log


router = APIRouter()


@router.post("/hook", tags=["HOOK"])
async def message(data: Dict, background_tasks: BackgroundTasks):
    """Recieve message from TG"""
    tb_log.log_info(f"{data}")
    # Dispatch message will be a method of Message Dispatcher
    background_tasks.add_task(dispatch_message, data)

    return {"result": "Message sent to dispatcher"}


#   This code will be moved to the Message Dispatcher
async def dispatch_message(data: Dict):
    """Send message to the message Dispatcher"""
    # The message dispatcher will:
    # parse the message
    # Put it in an apropriate Message Handler queue
    # Temporary - imideately send back an echo message
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"]
    answer = {
        "text": text,
        "chat_id": chat_id
    }

    await send_message(answer)
