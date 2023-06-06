"""

"""


from src.handlers import hnd
from src.mess_broker.schemas.processingdata import ProcessingData
from src.mess_broker.active_chats.active_chats import ActiveChats


class MessDispatcher:
    def __init__(self) -> None:
        self.__active_chats = ActiveChats()

    async def dispatch_message(self, data: ProcessingData | None):
        """Message dispatcher entry point"""
        if data is None:
            return
        # Set a new command
        self.__active_chats.set(data.hash_code, data)
        # Handle the data
        handler = hnd.get_handler_by_topic(data.text)
        await handler.handle(data)
