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
        self.__topics: list[Topic] = list()
        self.__default_topic = Topic()
        self.__load_topics()

    @property
    def type(self) -> str:
        return self.__type

    def fit(self, data: ProcessingData) -> bool:
        '''Check that the handler may handle the data'''
        return self.__get_topic(data) != self.__default_topic

    async def handle(self, data: ProcessingData) -> None:
        ''''''
        topic = self.__get_topic(data)
        content = topic.content
        if topic != self.__default_topic:
            content = tplst.get_content(topic)
        r_id = topic.redirection_id
        if r_id is not None and r_id != "":
            data.sender_id = r_id
        await self.__send_answer(data, content)

    def __get_topic(self, data: ProcessingData) -> Topic:
        ''''''
        for topic in self.__topics:
            # Check more criterions
            if (topic.name == data.command and
                    topic.service_alias == data.service_alias):
                return topic
        return self.__default_topic

    def __load_topics(self) -> None:
        """"""
        if self.__type != "default":
            self.__topics = tplst.topics_by_type(self.__type)

    async def __send_answer(self,
                            data: ProcessingData,
                            content):
        """Messanger exit point"""
        answer = self._create_answer(data, content)
        await services.send_message(answer)

    def _create_answer(self,
                       data: ProcessingData,
                       content: str) -> AnsweringData:
        """Create answer from topic"""
        return AnsweringData(
            service_type=data.service_type,
            service_alias=data.service_alias,
            sender_id=data.sender_id,
            content=content)
