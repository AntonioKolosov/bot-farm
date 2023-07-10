'''

'''


from src.proc_data.schemas.answeringdata import AnsweringData
from src.proc_data.schemas.processingdata import ProcessingData
from src.handlers.handler import Handler


class SimpleHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type="simple")

    def _create_answer(self,
                       data: ProcessingData,
                       content: str) -> AnsweringData:
        """Create answer from topic"""
        return AnsweringData(
            service_type=data.service_type,
            service_id=data.service_id,
            sender_id=data.sender_id,
            content=content)
