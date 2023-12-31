"""
Service metadata.
Include: metadata for setup commands,
and metadata for
"""


from typing import Optional
from pydantic import BaseModel


class CommandMetadata(BaseModel):
    name: str
    menu: bool
    button: bool
    type: str
    description: str
    content: str
    redirection_id: Optional[list] = []


class ServiceMetadata(BaseModel):
    id: int
    service_type: str
    service_alias: str
    chats_ids: list
    commands: list[CommandMetadata]
