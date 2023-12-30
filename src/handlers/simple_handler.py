"""
Handler which can work with text data(str format)
"""


from .handler import Handler
from .constants import HANDLER_TYPE_SIMPLE


class SimpleHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type=HANDLER_TYPE_SIMPLE)
