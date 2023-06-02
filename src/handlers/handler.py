'''
Base class for message handlers
'''


# from src.clients.tgclientmessage import send_message
# from src.clients import clpool
from src.clients.tgclient.tgclientmessage import send_message
from src.handlers.schemas.topic import Topic
from src.handlers.topics_loader import load_topics_by_type
from src.messanger.schemas.processingdata import ProcessingData


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
        answer = {
            "chat_id": data.sender_id,
            "text": topic.content
        }
        await self.__send_answer(answer)

    def __load_topics(self) -> None:
        """"""
        if self.__type != "default":
            self.__topics = load_topics_by_type(self.__type)

    # TODO: Temporary, will be via clients pool
    async def __send_answer(self, answer: dict):
        """Messanger exit point"""
        await send_message(answer)
        # await clpool.send_message(data.client, data.sender_id, answer)
