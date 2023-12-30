"""
Data format of answers.
Creates in Handler -> __create_answer
"""


from pydantic import BaseModel


class AnsweringData(BaseModel):
    service_type: str
    service_alias: str
    receiver_id: int | str
    content: str
