"""
Handler which setup menu and keyboads buttons
"""


from ..data_def.schemas.answeringdata import AnsweringData
from ..data_def.schemas.processingdata import ProcessingData
from ..data_def.schemas.service_md import CommandMetadata
from ..services import services
from .handler import Handler
from .constants import HANDLER_TYPE_START


class StartHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type=HANDLER_TYPE_START)

    def _get_answer_content(self,
                            cmd_data: CommandMetadata,
                            proc_data: ProcessingData) -> str:
        """"""
        return str(proc_data.sender_id)

    async def _send_answer(self, answer: AnsweringData):
        """"""
        await services.set_buttons(answer)
