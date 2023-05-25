"""

"""


from pydantic import BaseModel


class ProcessingData(BaseModel):
    client: int
    sender_id: int
    hash_code: str
    is_command: bool
    date: int
    text: str
