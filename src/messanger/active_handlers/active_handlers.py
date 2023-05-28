'''
'''


from src.handlers.handler import Handler
from src.handlers.internal_handler import InternalHandler


class ActiveHandlers:
    def __init__(self) -> None:
        self.__active_handlers: dict[str, Handler] = dict()
        # Always register the internal handler
        handler = InternalHandler()
        self.register(handler)

    def register(self, handler: Handler) -> None:
        ''''''
        self.__active_handlers[handler.id] = handler

    def unregister(self, id: str) -> None:
        ''''''
        self.__active_handlers.pop(id)

    def get_handler_by_id(self, id: str) -> Handler:
        ''''''
        return self.__active_handlers.get(id, InternalHandler())

    def get_handler_by_command(self, command: str) -> Handler | None:
        ''''''
        for id, handler in self.__active_handlers.items():
            if command in handler.commands:
                return self.__active_handlers.get(id)
