'''

'''


from src.handlers.handler import Handler


class SimpleHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type="simple")
        self._load_handler_topics()
