"""

"""


from src.clients.tgclient.tgclientmessage import send_message
from src.messanger.schemas.processingdata import ProcessingData
from src.messanger.active_chats.active_chats import ActiveChats
from src.messanger.active_handlers.active_handlers import ActiveHandlers


class MessDispatcher:
    def __init__(self) -> None:
        self.__active_chats = ActiveChats()
        self.__active_handlers = ActiveHandlers()
        self.__set_commands()

    async def dispatch_message(self, data: ProcessingData):
        """Messanger entry point"""
        if self.__iscommand(data.text):
            # Set a new command
            self.__active_chats.set(data.hash_code, data)
        if self.__active_chats.is_new(data.hash_code):
            # warning - the new chat starts without any command
            answer = {
                "chat_id": data.sender_id,
                "text": "A conversation has to start from a command"
            }
        else:
            # Handle the data
            command = self.__active_chats.get_command(data.hash_code)
            handler = self.__active_handlers.get_handler_by_command(command)
            if handler is None:
                answer = {
                    "chat_id": data.sender_id,
                    "text": ""
                }
            else:
                answer = handler.handle(command, data)
        await self.send_answer(answer)
        return

    @staticmethod
    def __iscommand(text: str):
        """"""
        return text.startswith("/")

    # TODO: Temporary, will be via clients pool
    async def send_answer(self, data: dict):
        """Messanger exit point"""
        await send_message(data)

    # TODO: Temporary, will be via clients pool
    def __set_commands(self) -> None:
        ''''''
        ...
        # res = await t_sp.set_commands(cmd_list)
        # return {"Commands": f"Set {res}"}
