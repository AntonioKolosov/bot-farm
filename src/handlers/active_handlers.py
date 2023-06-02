'''
'''


from src.handlers.handler import Handler
from src.handlers.simple_handler import SimpleHandler


class ActiveHandlers:
    def __init__(self) -> None:
        self.__active_handlers: dict[str, Handler] = dict()
        self.__default_handler = Handler()
        # Always register the internal simple handler
        self.register(SimpleHandler())

    def register(self, handler: Handler) -> None:
        ''''''
        self.__active_handlers[handler.id] = handler

    def unregister(self, id: str) -> None:
        ''''''
        self.__active_handlers.pop(id)

    def get_handler_by_topic(self, topic_name: str) -> Handler:
        ''''''
        for id, handler in self.__active_handlers.items():
            for topic in handler.topics:
                if topic_name == topic.name:
                    return handler
        return self.__default_handler

    def get_topics_names(self) -> list[str]:
        """"""
        names = list()
        for id, handler in self.__active_handlers.items():
            for topic in handler.topics:
                names.append(topic.name)
        return names