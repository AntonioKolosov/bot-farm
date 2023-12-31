"""
Handlers which connected with our service:
    1.Simple Handler
    2.Default Handler
    3.Subtitles Handler
"""


from src.handlers.start_handler import StartHandler
from src.data_def.schemas.processingdata import ProcessingData
from src.data_def.schemas.service_md import ServiceMetadata, CommandMetadata
from src.loaders import loader
from src.handlers.handler import Handler
from src.handlers.simple_handler import SimpleHandler
from src.handlers.subtitles_handler import SubtitlesHandler


class ActiveHandlers:
    def __init__(self) -> None:
        self.__active_handlers: dict[str, Handler] = dict()
        self.__default_handler = Handler()
        # Always register each existing handler
        # self.__get_breaf_topics
        self.register(SimpleHandler())
        self.register(StartHandler())
        self.register(SubtitlesHandler())

    def register(self, handler: Handler) -> None:
        """Registered Handlers -> mess_broker"""
        self.__active_handlers[handler.type] = handler

    def unregister(self, type: str) -> None:
        """Automatically remove unregistered handlers"""
        self.__active_handlers.pop(type)

    def get_command_handler(self, cmd_data: CommandMetadata) -> Handler:
        """Choose Handler with command_metadata"""
        for _, handler in self.__active_handlers.items():
            if handler.type == cmd_data.type:
                return handler
        return self.__default_handler

    def get_command_metadata(self, data: ProcessingData):
        """Recieve command metadata"""
        md_name = f'{data.service_type}___{data.service_alias}'.lower()
        metadata = loader.load_metadata(md_name)
        # Construct service_meta_data_object
        service_metadata = ServiceMetadata(**metadata)
        return [command for
                command in service_metadata.commands
                if data.command == command.name][0]
