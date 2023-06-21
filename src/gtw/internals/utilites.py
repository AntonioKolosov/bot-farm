"""
The gtw utilites
"""


import hashlib
from src.gtw.schemas.tgindata import TgInData
from src.proc_data.schemas.processingdata import ProcessingData


def tg_data_converter(bot_id: str, data) -> ProcessingData | None:
    '''Convert TG data to the unified format
    of message broker processing data'''
    tgindata: TgInData = TgInData(**data)
    message = tgindata.tg_message()
    if message is None:
        return None
    return ProcessingData(service_type="TG",
                          service_id=bot_id,
                          sender_id=message.chat.id,
                          hash_code=tg_hash_md5(tgindata.get_const_data()),
                          is_command=message.text.startswith('/'),
                          date=message.date,
                          text=message.text)


def tg_hash_md5(data) -> str:
    '''Hashes a not nested dict'''
    dhash = hashlib.md5()
    encoded = data.encode()
    dhash.update(encoded)
    hash = dhash.hexdigest()
    return hash
