"""

"""


from pydantic import BaseModel


class ProcessingData(BaseModel):
    service_type: str
    service_alias: str
    sender_id: int | str
    hash_code: str
    is_command: bool
    date: int
    command: str
