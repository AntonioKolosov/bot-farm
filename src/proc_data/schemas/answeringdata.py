"""

"""


from pydantic import BaseModel


class AnsweringData(BaseModel):
    service_type: str
    service_id: str
    sender_id: int
    content: str
