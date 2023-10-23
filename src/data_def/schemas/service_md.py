"""
Service metadata
"""


from typing import Optional
from pydantic import BaseModel


class CommandMetadata(BaseModel):
    name: str
    type: str
    description: str
    content: str
    redirection_id: Optional[list] = []


class ServiceMetadata(BaseModel):
    id: int
    service_type: str
    service_alias: str
    buttons: list
    chats_ids: list
    commands: list[CommandMetadata]
