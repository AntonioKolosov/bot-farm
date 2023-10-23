"""
Dispatch a message for an appropriate handler
"""


from src.handlers import hnd
from src.data_def.schemas.processingdata import ProcessingData


class MessDispatcher:
    def __init__(self) -> None:
        ''''''

    async def dispatch_message(self, data: ProcessingData | None):
        """Message dispatcher entry point"""
        if data is None:
            return

        cmd_metadata = hnd.get_command_metadata(data)
        # Handle the data
        handler = hnd.get_command_handler(cmd_metadata)
        await handler.handle(data, cmd_metadata)
