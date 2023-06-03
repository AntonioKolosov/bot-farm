"""

"""


import json
import os

from src.startup.startup import Startup
from src.startup.tgstartup.tgstartup import TgStartup


class StartupList:
    """"""
    def __init__(self) -> None:
        """"""
        self.__bot_list = []
        # Read BOT_LIST from env
        self.__bot_types_list = json.loads(
            os.environ.get("BOT_TYPES_LIST", '["TG"]')
        )
        # Iteration throught BOT_LIST
        for bt in self.__bot_types_list:
            print(bt)
            # Create Startup objects for each bot types
            startup = self.__startup_factory(bt)
            # Store it into list
            self.__bot_list.append(startup)

    def __startup_factory(self, type: str) -> Startup:
        """Create Startup objects regarding bot type"""
        if type == "TG":
            return TgStartup()
        return Startup(type="")

    def startup(self) -> None:
        """"""
        for b in self.__bot_list:
            print("STARTUP", b.type)
