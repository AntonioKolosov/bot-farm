'''

'''


from src.proc_data.schemas.answeringdata import AnsweringData
from src.proc_data.schemas.processingdata import ProcessingData
from src.services import services
from src.handlers.handler import Handler


class SimpleHandler(Handler):
    def __init__(self) -> None:
        super().__init__(id="simple", type="simple")

    async def _send_answer(self,
                           data: ProcessingData,
                           content: str):
        """Messanger exit point"""
        answer = AnsweringData(
            service_type=data.service_type,
            service_id=data.service_id,
            sender_id=data.sender_id,
            content=content)
        await services.send_message(answer)
