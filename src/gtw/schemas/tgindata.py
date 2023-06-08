"""
Hashing from: https://www.pythoncentral.io/hashing-strings-with-python/
"""


import json
from typing import Optional
from pydantic import BaseModel, Field


class TgChat(BaseModel):
    id: int
    first_name: str
    username: Optional[str]
    type: str


class TgFrom(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: Optional[str]
    language_code: str
    is_premium: Optional[bool]


class TgMessage(BaseModel):
    message_id: int
    from_: TgFrom = Field(alias='from')
    chat: TgChat
    date: int
    edit_date: Optional[int]
    text: str


class TgInData(BaseModel):
    update_id: int
    message: Optional[TgMessage]
    edited_message: Optional[TgMessage]

    def tg_message(self) -> TgMessage | None:
        '''Get message data'''
        return (self.message if self.message is not None
                else self.edited_message)

    def get_const_data(self) -> str:
        '''Get not mutable data from incoming data'''
        message: TgMessage | None = self.tg_message()
        if message is not None:
            from_ = str(json.dumps(message.from_.dict(), sort_keys=True))
            chat = str(json.dumps(message.chat.dict(), sort_keys=True))
            return f'{from_}-{chat}'
        else:
            return ""
