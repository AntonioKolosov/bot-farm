"""
The gtw utilites
"""


import hashlib
from src.clients.clientpool import ClientCode
from src.gtw.schemas.tgindata import TgInData
from src.messanger.schemas.processingdata import ProcessingData


def tg_data_converter(bot_id: int, data: dict) -> ProcessingData:
    '''Convert TG data to the unified format
    of messanger processing data'''
    tgindata: TgInData = TgInData(**data)
    message = tgindata.tg_message()
    return ProcessingData(client_type=ClientCode.TG,
                          endpoint_id=bot_id,
                          sender_id=message.chat.id,
                          hash_code=tg_hash_md5(tgindata.get_const_data()),
                          is_command=message.text.startswith('/'),
                          date=message.date,
                          text=message.text)


def tg_hash_md5(data: dict) -> str:
    '''Hashes a not nested dict'''
    dhash = hashlib.md5()
    encoded = data.encode()
    dhash.update(encoded)
    hash = dhash.hexdigest()
    return hash
