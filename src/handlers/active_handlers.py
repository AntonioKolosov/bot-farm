'''
'''


from src.services import services
from src.proc_data.schemas.processingdata import ProcessingData
from src.handlers.handler import Handler
from src.handlers.simple_handler import SimpleHandler
from src.handlers.subtitles_handler import SubtitlesHandler
from src.topics import tplst


class ActiveHandlers:
    def __init__(self) -> None:
        self.__active_handlers: dict[str, Handler] = dict()
        self.__default_handler = Handler()
        # Always register each existing handler
        self.register(SimpleHandler())
        self.register(SubtitlesHandler())
        # self.register(YourHandler())
        breaf_topics = self.__get_breaf_topics()
        services.set_breaf_topics(breaf_topics)

    def register(self, handler: Handler) -> None:
        ''''''
        self.__active_handlers[handler.type] = handler

    def unregister(self, type: str) -> None:
        ''''''
        self.__active_handlers.pop(type)

    def get_handler_for_data(self, data: ProcessingData) -> Handler:
        ''''''
        for id, handler in self.__active_handlers.items():
            if handler.fit(data):
                return handler
        return self.__default_handler

    def __get_breaf_topics(self) -> list[dict[str, str]]:
        """"""
        return tplst.breaf_topics()
