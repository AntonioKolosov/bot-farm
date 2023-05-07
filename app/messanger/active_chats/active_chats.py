"""

"""


from typing import Tuple


class ActiveChats:
    def __init__(self) -> None:
        self.__active_chats = []

    @property
    def active_chats(self):
        """Collection of active chats"""
        return self.__active_chats

    def add_chat(self, global_id: Tuple[int, str]):
        """Analize Global ID and Active Chats"""
        chat_id, text = global_id
        if self.__iscommand(text):
            if chat_id in self.__active_chats:
                # Replace an item with this chat_id(replace)
                self.__active_chats = list(map
                                           (lambda x: x.replace(x.text, text),
                                            self.__active_chats))
            else:
                self.__active_chats.append(chat_id)
        elif chat_id not in self.__active_chats:
            # Unknown conversation
            return False
        else:
            pass
        return True

    def remove_chat(self, global_id):
        """Remove item"""

    @staticmethod
    def __iscommand(text: str):
        """"""
        return text.startswith("/")
