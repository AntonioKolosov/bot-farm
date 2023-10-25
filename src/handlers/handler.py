'''
Base class for message handlers
'''


from ..data_def.schemas.processingdata import ProcessingData
from ..data_def.schemas.service_md import CommandMetadata
from ..data_def.schemas.answeringdata import AnsweringData
from ..loaders import loader
from ..services import services
from . constants import HANDLER_TYPE_DEFAULT, CONTENT_REF, RETURN_TO_SENDER


class Handler:
    def __init__(self, type: str = HANDLER_TYPE_DEFAULT) -> None:
        self.__type: str = type

    @property
    def type(self) -> str:
        return self.__type

    async def handle(self,
                     proc_data: ProcessingData,
                     cmd_data: CommandMetadata) -> None:
        ''''''
        receivers = self.__receivers(proc_data, cmd_data)
        answer = self.__create_answer(proc_data, cmd_data)
        for receiver in receivers:
            if (receiver != RETURN_TO_SENDER):
                answer.receiver_id = receiver
            if (answer.content != ''):
                await self._send_answer(answer)

    def __receivers(self,
                    data: ProcessingData,
                    cmd_data: CommandMetadata) -> list[int | str]:
        ''' '''
        if (cmd_data.redirection_id is not None
                and len(cmd_data.redirection_id) != 0):
            return cmd_data.redirection_id
        return [data.sender_id]

    async def _send_answer(self, answer: AnsweringData,):
        """Messanger exit point"""
        await services.send_message(answer)

    def __create_answer(
            self,
            proc_data: ProcessingData,
            cmd_data: CommandMetadata) -> AnsweringData:
        """Create answer for command"""
        # command's type specific
        topic_data = self._get_answer_content(cmd_data, proc_data.hash_code)
        return AnsweringData(
            service_type=proc_data.service_type,
            service_alias=proc_data.service_alias,
            receiver_id=proc_data.sender_id,
            content=topic_data)

    def _get_answer_content(self, cmd_data: CommandMetadata, hash: str) -> str:
        ''' topic's type specific '''
        content = cmd_data.content
        if (cmd_data.content.startswith(CONTENT_REF)):
            ref = cmd_data.content[len(CONTENT_REF):]
            location = f"{cmd_data.type}/{ref}"
            content = loader.load_data_text(location)
        return content
