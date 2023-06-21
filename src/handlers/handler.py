'''
Base class for message handlers
'''


from src.services import services
from src.topics import Topic, load_topics_by_type
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

    @property
    def topics(self) -> list[Topic]:
        return self.__topics

    async def handle(self, data: ProcessingData) -> None:
        ''''''
        topic = self.__default_topic
        for topic in self.__topics:
            if topic.name == data.text:
                break
        await self.__send_answer(data, topic)

    def __load_topics(self) -> None:
        """"""
        if self.__type != "default":
            self.__topics = load_topics_by_type(self.__type)

    async def __send_answer(self, data: ProcessingData, topic: Topic):
        """Messanger exit point"""
        # Patch for /start command
        if data.text == "/start":
            topic.content = ""
        answer = {
            "chat_id": data.sender_id,
            "text": topic.content
        }
        await services.send_message(data.service_type, data.service_id, answer)
