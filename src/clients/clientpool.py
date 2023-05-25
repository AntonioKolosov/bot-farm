'''Base class for messangers clients'''


from enum import Enum

from src.clients.client import Client
# from src.clients.tgclient.tgclient import TgClient


class ClientCode(int, Enum):
    TG = 0
    WAP = 1


class ClientPool():
    def __init__(self) -> None:
        self.__clients = dict[ClientCode, Client]

    # def init(self) -> None:
    #     ''''''
    #     # TODO: load all clients
    #     self.__clients[ClientCode.TG] = TgClient()

    async def send_message(self, code: ClientCode, mess: dict) -> bool:
        ''''''
        ...
