from fastapi import APIRouter, BackgroundTasks

# from ..schemas.tbdata import TBData
from src.gtw.internals.tbotlogger import tb_log
from src.gtw.schemas.tgindata import TgInData
from src.messanger.mess_dispatcher.mess_dispatcher import MessDispatcher
from src.messanger.schemas.processingdata import ProcessingData


router = APIRouter()

dsp = MessDispatcher()


@router.post("/tgdata", tags=["TGDATA"])
async def message(data: TgInData, background_tasks: BackgroundTasks):
    """Recieve message from TG"""
    tb_log.log_info(f"{data}")
    # Dispatch message will be a method of Message Dispatcher
    processing_data = tg_data_converter(data)
    background_tasks.add_task(dsp.dispatch_message, processing_data)

    return {"result": "Message sent to dispatcher"}


def tg_data_converter(data: TgInData) -> ProcessingData:
    """"""
    message = data.tg_message()
    if message is None:
        raise Exception("DataError")
    return ProcessingData(client=0,
                          sender_id=message.chat.id,
                          hash_code=data.tg_hash_md5(),
                          is_command=True,
                          date=message.date,
                          text=message.text)
