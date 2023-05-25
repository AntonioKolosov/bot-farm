"""

"""


from typing import Dict

from src.clients.tgclient.tgclientmessage import send_message
from src.messanger.schemas.processingdata import ProcessingData


class MessDispatcher:
    def __init__(self) -> None:
        """"""

    def dispatch_message(self, data: ProcessingData):
        """Messanger entry point"""
        #   This code will be moved to the Message Dispatcher
        # The message dispatcher will:
        # parse the message
        # Put it in an apropriate Message Handler queue
        # Temporary - imideately send back an echo message
        # Global ID for searching active chat
        # global_id = self.__parser.pars_incoming_message(data)
        # if self.__active_chats.add_chat(global_id):
        #     # Put the message to queue
        #     return True
        # return False

    async def send_answer(self, data: Dict):
        """Messanger exit point"""
        await send_message(data)
