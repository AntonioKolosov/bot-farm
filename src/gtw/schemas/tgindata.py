"""
Hashing from: https://www.pythoncentral.io/hashing-strings-with-python/
"""


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
            hash_from = f'{message.from_.id}-{message.from_.first_name}'
            hash_chat = f'{message.chat.id}-{message.chat.first_name}'
            return f'{hash_from}--{hash_chat}'
        else:
            return ""
