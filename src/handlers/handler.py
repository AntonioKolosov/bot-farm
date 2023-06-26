'''
Base class for message handlers
'''


from src.services import services
from src.topics import tplst, Topic
from src.proc_data.schemas.processingdata import ProcessingData


class Handler:
    def __init__(self, id: str = "default", type: str = "default") -> None:
        self.__id: str = id
        self.__type: str = type
        self.__topics: list[Topic] = list()
        self.__default_topic = Topic()
        self.__load_topics()

    @property
    def id(self) -> str:
        return self.__id

    def fit(self, data: ProcessingData) -> bool:
        '''Check that the handler may handle the data'''
        return self.__get_topic(data) != self.__default_topic

    async def handle(self, data: ProcessingData) -> None:
        ''''''
        topic = self.__get_topic(data)
        topic.content = tplst.get_content(topic)
        await self.__send_answer(data, topic)

    def __get_topic(self, data: ProcessingData) -> Topic:
        ''''''
        alias = services.get_alias(data.service_type, data.service_id)
        for topic in self.__topics:
            # Check more criterions
            if topic.name == data.text and topic.service_id == alias:
                return topic
        return self.__default_topic

    def __load_topics(self) -> None:
        """"""
        if self.__type != "default":
            self.__topics = tplst.topics_by_type(self.__type)

    async def __send_answer(self, data: ProcessingData, topic: Topic):
        """Messanger exit point"""
        answer = {
            "chat_id": data.sender_id,
            "text": topic.content
        }
        await services.send_message(data.service_type, data.service_id, answer)
