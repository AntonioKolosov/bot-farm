"""

"""


from src.handlers import topic_handler, topics_names
from src.messanger.schemas.processingdata import ProcessingData
from src.messanger.active_chats.active_chats import ActiveChats


class MessDispatcher:
    def __init__(self) -> None:
        self.__active_chats = ActiveChats()

    async def dispatch_message(self, data: ProcessingData):
        """Messanger entry point"""
        # Set a new command
        self.__active_chats.set(data.hash_code, data)
        # Handle the data
        handler = topic_handler(data.text)
        await handler.handle(data)

    def topics_names(self) -> list[dict[str, str]]:
        """Return topics names"""
        return topics_names()
