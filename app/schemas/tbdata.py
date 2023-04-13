"""
"""


from pydantic import BaseModel, Field


class TBChat(BaseModel):
    id: int
    first_name: str
    username: str
    type: str


class TBFrom(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: str
    language_code: str
    is_premium: bool


class TBMessage(BaseModel):
    message_id: int
    from_: TBFrom = Field(alias='from')
    chat: TBChat
    date: int
    text: str


class TBData(BaseModel):
    update_id: int
    message: TBMessage
