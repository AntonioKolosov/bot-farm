"""
The gtw utilites includes two converters:
    1. from tg_incoming_data to proccesing_data
    2. from answering_data to telegram_data
"""


import hashlib
from src.gtw.schemas.tgindata import TgInData
from src.data_def.schemas.processingdata import ProcessingData
from src.data_def.schemas.answeringdata import AnsweringData


def tg_data_converter(alias: str, data) -> ProcessingData | None:
    """Convert TG data to the unified format
    of message broker processing data"""
    tgindata: TgInData = TgInData(**data)
    message = tgindata.tg_message()
    if message is None:
        return None
    if message.text is None:
        return None
    return ProcessingData(service_type="TG",
                          service_alias=alias,
                          sender_id=message.chat.id,
                          hash_code=tg_hash_md5(tgindata.get_const_data()),
                          is_command=message.text.startswith('/'),
                          date=message.date,
                          command=message.text)


def tg_hash_md5(data) -> str:
    """Hashes a not nested dict"""
    dhash = hashlib.md5()
    encoded = data.encode()
    dhash.update(encoded)
    hash = dhash.hexdigest()
    return hash


def tg_answer_converter(bot_id, answer: AnsweringData) -> dict:
    """Convert Answering Data to Telegram format"""
    tg_answer = {
        "bot_id": bot_id,
        "chat_id": answer.receiver_id,
        "text": answer.content,
    }
    return tg_answer
