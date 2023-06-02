from fastapi import APIRouter, BackgroundTasks, Request

from src.gtw.internals.utilites import tg_data_converter
from src.messanger.mess_dispatcher import dispatch
from src.gtw.internals.tbotlogger import tb_log


router = APIRouter()


@router.post("/tgincdata", tags=["TGINDATA"])
async def tg_inc_data(request: Request, background_tasks: BackgroundTasks):
    """Recieve message from TG"""
    data = await request.json()
    tb_log.log_info(data)

    # Convert to the unified format of the messanger
    processing_data = tg_data_converter(data)
    # Process the data in a background
    background_tasks.add_task(dispatch, processing_data)

    return {"result": "Message sent to the dispatcher"}
