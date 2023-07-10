'''

'''


from src.proc_data.schemas.answeringdata import AnsweringData
from src.proc_data.schemas.processingdata import ProcessingData
from src.handlers.handler import Handler


class SimpleHandler(Handler):
    def __init__(self) -> None:
        super().__init__(id="simple", type="simple")

    async def _send_answer(self,
                           data: ProcessingData,
                           content):
        """Messanger exit point"""
        # answer = self._create_answer(data, content)
        # await services.send_message(answer)

    def _create_answer(self,
                       data: ProcessingData,
                       content: str) -> AnsweringData:
        """Create answer from topic"""
        return AnsweringData(
            service_type=data.service_type,
            service_id=data.service_id,
            sender_id=data.sender_id,
            content=content)
