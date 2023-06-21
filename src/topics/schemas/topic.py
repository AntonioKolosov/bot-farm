"""
"""

from pydantic import BaseModel


class Topic(BaseModel):
    id: int = 0
    name: str = "/default"
    description: str = "anydata"
    type: str = "default"
    service_type: str = ""
    service_id: str = ""
    content: str = ("Brief help topic: \n \
                    Use a command from the bot menu")
