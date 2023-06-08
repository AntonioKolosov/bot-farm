"""
"""


from src.mess_broker.schemas.processingdata import ProcessingData


class ActiveChats:
    def __init__(self) -> None:
        self.__active_chats: dict[str, ProcessingData] = dict()

    def is_new(self, hash_code: str) -> bool:
        """True if it is the first message from the chat"""
        return hash_code not in self.__active_chats

    def set(self, hash_code: str, item: ProcessingData):
        """ Active Chats"""
        self.__active_chats[hash_code] = item

    def remove(self, hash_code):
        """Remove item"""
        self.__active_chats.pop(hash_code)

    def get_command(self, hash_code):
        """Get item text (command)"""
        empty_data = ProcessingData(
            client=0,
            sender_id=0,
            hash_code="",
            is_command=True,
            date=0,
            text="Chat Not Found")
        return self.__active_chats.get(hash_code, empty_data).text
