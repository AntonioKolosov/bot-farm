'''
Base class for message handlers
'''


from ..proc_data.schemas.answeringdata import AnsweringData
from ..proc_data.schemas.processingdata import ProcessingData
from ..services import services
from ..topics import tplst, Topic
from . constants import HANDLER_TYPE_DEFAULT, CONTENT_REF_PREFIX


class Handler:
    def __init__(self, type: str = HANDLER_TYPE_DEFAULT) -> None:
        self.__type: str = type

    @property
    def type(self) -> str:
        return self.__type

    def fit(self, data: ProcessingData) -> bool:
        '''Check that the handler may handle the data'''
        topic = self.__get_topic(data)
        return (self.type == topic.metadata.type
                and topic.name == data.command
                and topic.metadata.service_type == data.service_type
                and topic.metadata.service_alias == data.service_alias)

    async def handle(self, data: ProcessingData) -> None:
        ''''''
        topic = self.__get_topic(data)
        receivers = self.__receivers(data, topic)
        for receiver in receivers:
            answer = self.__create_answer(data, receiver, topic)
            await self._send_answer(answer)

    def __receivers(self,
                    data: ProcessingData,
                    topic: Topic) -> list[int | str]:
        ''' '''
        if (topic.metadata.redirection_id is not None
                and len(topic.metadata.redirection_id) != 0):
            return topic.metadata.redirection_id
        return [data.sender_id]

    def __get_topic(self, data: ProcessingData) -> Topic:
        ''''''
        topic = tplst.get_topic(data.command,
                                data.service_type,
                                data.service_alias)
        return topic

    async def _send_answer(self, answer: AnsweringData,):
        """Messanger exit point"""
        await services.send_message(answer)

    def __create_answer(
            self,
            data: ProcessingData,
            receiver: int | str,
            topic: Topic) -> AnsweringData:
        """Create answer from topic"""
        # topic's type specific
        topic_data = self._get_answer_content(topic, data.hash_code)
        return AnsweringData(
            service_type=data.service_type,
            service_alias=data.service_alias,
            receiver_id=receiver,
            content=topic_data)

    def _get_answer_content(self, topic: Topic, hash: str) -> str:
        ''' topic's type specific '''
        topic_data = topic.metadata.content
        if (topic_data.startswith(CONTENT_REF_PREFIX)):
            ref = topic_data[len(CONTENT_REF_PREFIX):]
            location = f"{topic.metadata.type}/{ref}"
            topic_data = topic.get_topic_data_text(location)
        return topic_data
