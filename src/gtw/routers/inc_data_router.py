"""
Telegram incoming data router
"""


from fastapi import APIRouter, BackgroundTasks, Request

from src.data_def.utilites import tg_data_converter
from src.mess_broker import dsp
from src.internals.tbotlogger import tb_log


router = APIRouter()


@router.post("/tgincdata/{alias}", tags=["TGINDATA"])
async def tg_inc_data(request: Request,
                      alias: str,
                      background_tasks: BackgroundTasks):
    """Recieve message from TG"""
    data = await request.json()
    tb_log.log_info(data)

    # Convert to the unified format of the message broker
    processing_data = tg_data_converter(alias, data)
    # Process the data in a background
    background_tasks.add_task(dsp.dispatch_message, processing_data)

    return {"result": "Message sent to the dispatcher"}
