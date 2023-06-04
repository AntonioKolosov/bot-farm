from fastapi import APIRouter, BackgroundTasks, Request

from src.gtw.internals.utilites import tg_data_converter
from src.messanger.mess_dispatcher import dsp
from src.gtw.internals.tbotlogger import tb_log


router = APIRouter()


@router.post("/tgincdata/{bot_id}", tags=["TGINDATA"])
async def tg_inc_data(request: Request,
                      bot_id: int,
                      background_tasks: BackgroundTasks):
    """Recieve message from TG"""
    data = await request.json()
    tb_log.log_info(data)

    # Convert to the unified format of the messanger
    processing_data = tg_data_converter(bot_id, data)
    # Process the data in a background
    background_tasks.add_task(dsp.dispatch_message, processing_data)

    return {"result": "Message sent to the dispatcher"}
