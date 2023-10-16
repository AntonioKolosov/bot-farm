"""
Service metadata
"""


from pydantic import BaseModel


class CommandMetadata(BaseModel):
    name: str
    type: str
    service_type: str
    service_alias: str
    description: str
    content: str


class ServiceMetadata(BaseModel):
    id: int
    buttons: list
    chats_ids: list
    commands: list[CommandMetadata]
