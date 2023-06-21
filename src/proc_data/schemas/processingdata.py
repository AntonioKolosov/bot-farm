"""

"""


from pydantic import BaseModel


class ProcessingData(BaseModel):
    service_type: str
    service_id: str
    sender_id: int
    hash_code: str
    is_command: bool
    date: int
    text: str
