"""

"""


from src.mess_broker.mess_dispatcher.schemas.service_md import ServiceMetadata
from src.handlers import hnd
from src.proc_data.schemas.processingdata import ProcessingData
from src.mess_broker.active_chats.active_chats import ActiveChats
from src.topics.loaders import loader


class MessDispatcher:
    def __init__(self) -> None:
        self.__active_chats = ActiveChats()

    async def dispatch_message(self, data: ProcessingData | None):
        """Message dispatcher entry point"""
        if data is None:
            return

        type = self.get_topic_type(data)
        # Set a new command
        self.__active_chats.set(data.hash_code, data)
        # Handle the data
        handler = hnd.get_handler_by_type(type)
        await handler.handle(data)

    def get_topic_type(self, data: ProcessingData):
        md_name = f'{data.service_type}___{data.service_alias}'.lower()
        metadata = loader.load_metadata(md_name)
        # Construct service_meta_data_object
        service_metadata = ServiceMetadata(**metadata)
        command = [command for
                   command in service_metadata.commands
                   if data.command == command.name][0]

        return command.type
