"""

"""


from src.messanger.schemas.processingdata import ProcessingData
from src.messanger.active_chats.active_chats import ActiveChats
from src.messanger.active_handlers.active_handlers import ActiveHandlers


class MessDispatcher:
    def __init__(self) -> None:
        self.__active_chats = ActiveChats()
        self.__active_handlers = ActiveHandlers()

    async def dispatch_message(self, data: ProcessingData):
        """Messanger entry point"""
        # Set a new command
        self.__active_chats.set(data.hash_code, data)
        # Handle the data
        handler = self.__active_handlers.get_handler_by_topic(data)
        await handler.handle(data)
