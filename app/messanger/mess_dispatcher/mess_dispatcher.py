"""

"""


from typing import Dict

from app.tapiclient.tapiclientmessage import send_message
from app.messanger.mess_parser.mess_parser import MessParser
from app.messanger.active_chats.active_chats import ActiveChats


class MessDispatcher:
    def __init__(self) -> None:
        self.__parser = MessParser()
        self.__active_chats = ActiveChats()
        self.__queues_list = []

    def dispatch_message(self, data: Dict):
        """Messanger entry point"""
        #   This code will be moved to the Message Dispatcher
        # The message dispatcher will:
        # parse the message
        # Put it in an apropriate Message Handler queue
        # Temporary - imideately send back an echo message
        # Global ID for searching active chat
        global_id = self.__parser.pars_incoming_message(data)
        if self.__active_chats.add_chat(global_id):
            # Put the message to queue
            return True
        return False

    async def send_answer(self, data: Dict):
        """Messanger exit point"""
        await send_message(data)
