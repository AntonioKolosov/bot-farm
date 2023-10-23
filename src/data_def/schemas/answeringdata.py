"""

"""


from pydantic import BaseModel


class AnsweringData(BaseModel):
    service_type: str
    service_alias: str
    receiver_id: int | str
    content: str
