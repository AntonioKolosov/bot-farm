'''
Base class for message handlers
'''


from src.messanger.schemas.processingdata import ProcessingData


class Handler:
    def __init__(self, id: str, commands: list[str]) -> None:
        self.__id: str = id
        self.__commands: list[str] = commands
        self.__content: dict[str, str] = {}

    def handle(self, command: str, data: ProcessingData) -> dict:
        ''''''
        content = data.text
        if command == data.text:
            answer = f'command {command} - not supported by the handler'
            content = self.content.get(command, answer)
        return {
            "chat_id": data.sender_id,
            "text": content
        }

    @property
    def id(self) -> str:
        return self.__id

    @property
    def commands(self) -> list[str]:
        return self.__commands

    @property
    def content(self) -> dict[str, str]:
        ''''''
        return self.__content

    @content.setter
    def content(self, content: dict[str, str]) -> None:
        ''''''
        self.__content = content
