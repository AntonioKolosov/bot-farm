'''
'''


from src.handlers.handler import Handler
from src.handlers.default_handler import DefaultHandler
from src.messanger.schemas.processingdata import ProcessingData


class ActiveHandlers:
    def __init__(self) -> None:
        self.__active_handlers: dict[str, Handler] = dict()
        # Always register the internal handler
        handler = DefaultHandler()
        self.register(handler)

    def register(self, handler: Handler) -> None:
        ''''''
        self.__active_handlers[handler.id] = handler

    def unregister(self, id: str) -> None:
        ''''''
        self.__active_handlers.pop(id)

    def get_handler_by_topic(self, data: ProcessingData) -> Handler:
        ''''''
        handler = Handler()
        for k, v in self.__active_handlers.items():
            for t in v.topics:
                if data.text == t.name:
                    handler = v
            # TODO: send help data
        return handler
