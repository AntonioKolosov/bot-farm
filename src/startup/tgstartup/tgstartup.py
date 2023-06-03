"""
TG Startup module
"""


from src.startup.startup import Startup


class TgStartup(Startup):
    def __init__(self) -> None:
        """"""
        super().__init__(type="TG")
