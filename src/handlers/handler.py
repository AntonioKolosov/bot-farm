'''
Base class for message handlers
'''


from src.proc_data.schemas.answeringdata import AnsweringData
from src.services import services
from src.topics import tplst, Topic
from src.proc_data.schemas.processingdata import ProcessingData


class Handler:
    def __init__(self, type: str = "default") -> None:
        self.__type: str = type
        self._topics: list[Topic] = list()
        self._default_topic = Topic()
        self._load_handler_topics()

    @property
    def type(self) -> str:
        return self.__type

    def fit(self, data: ProcessingData) -> bool:
        '''Check that the handler may handle the data'''
        return self.__get_topic(data) != self._default_topic

    async def handle(self, data: ProcessingData) -> None:
        ''''''
        topic = self.__get_topic(data)
        receivers = self.__receivers(data, topic)
        for receiver in receivers:
            # topic's type specific
            answer = self._create_answer(data, receiver, topic)
            await self._send_answer(answer)

    def __receivers(self, data, topic) -> list[int | str]:
        ''' '''
        receivers = topic.redirection_id
        if receivers is not None and len(receivers) != 0:
            return receivers
        return [data.sender_id]

    def __get_topic(self, data: ProcessingData) -> Topic:
        ''''''
        for topic in self._topics:
            # Check more criterions
            if (topic.name == data.command and
                    topic.service_alias == data.service_alias):
                return topic
        return self._default_topic

    def _load_handler_topics(self) -> None:
        """"""
        if self.__type != "default":
            self._topics = tplst.topics_by_type(self.__type)

    async def _send_answer(self, answer: AnsweringData,):
        """Messanger exit point"""
        await services.send_message(answer)

    def _create_answer(self,
                       data: ProcessingData,
                       receiver: int | str,
                       topic: Topic) -> AnsweringData:
        """Create answer from topic"""
        topic_data = topic.content
        if topic != self._default_topic:
            location = f"{topic.type}/{topic.content}"
            topic_data = tplst.get_topic_data_text(location)
        return AnsweringData(
            service_type=data.service_type,
            service_alias=data.service_alias,
            receiver_id=receiver,
            content=topic_data)
