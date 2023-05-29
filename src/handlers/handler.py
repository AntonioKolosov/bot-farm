'''
Base class for message handlers
'''


import json

from src.clients.tgclient.tgclientmessage import send_message
from src.handlers.schemas.topic import Topic
from src.messanger.schemas.processingdata import ProcessingData


class Handler:
    def __init__(self, id: str = "default", type: str = "default") -> None:
        self.__id: str = id
        self.__type: str = type
        self.__topics: list[Topic] = []
        self.__load_topics()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def topics(self) -> list[Topic]:
        return self.__topics

    async def handle(self, data: ProcessingData) -> None:
        ''''''
        for topic in self.__topics:
            if data.text == topic.name:
                answer = {
                    "chat_id": data.sender_id,
                    "text": topic.content
                }
                await self.__send_answer(answer)

    def __load_topics(self) -> None:
        """"""
        with open(file="datatopics/topicfake.json", mode="r") as f:
            # topic_raw = json.load(f)
            topic_obj = json.load(f)
            # topic_obj = json.loads(topic_raw)
            topic = Topic(**topic_obj)
        self.__topics.append(topic)

    # TODO: Temporary, will be via clients pool
    async def __send_answer(self, data: dict):
        """Messanger exit point"""
        await send_message(data)
