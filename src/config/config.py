import os
from dotenv import load_dotenv


class Configuration:
    """
    Includes configs for:
        1. Logger
        2. Services
        3. Loader
    """
    def __init__(self) -> None:
        load_dotenv()
        # Logger
        self.log_level = os.environ.get("LOG_LEVEL", "WARNING")
        self.log_path = os.environ.get("LOG_PATH", "twbot.log")

        # Services
        bot_types = os.environ.get("BOT_TYPES_LIST",
                                   "[\"error:error\"]")
        self.bot_types_list = list(map(str, bot_types[1:-1].split(",")))

        tokens = os.environ.get("TG_BOTS_TOKENS",
                                "[\"error:error\"]")
        self.tokens = list(map(str, tokens[1:-1].split(",")))
        self.gtw_url = os.environ.get("GTW_URL", "")
        bots_id_2_names = os.environ.get("TG_BOTS_ID_2_NAMES",
                                         "[\"error:error\"]")
        self.bots_id_2_names = list(map(str,
                                        bots_id_2_names[1:-1].split(",")))

        # Loader
        self.loader_type = os.environ.get("TOPICS_LOADER_TYPE", "BASE")
        if self.loader_type == "MONGO":
            self.storage = (os.environ.get("DB_MONGO_URI", "")
                            + "-----"
                            + os.environ.get("DB_MONGO_NAME", ""))
            self.df_storage = (os.environ.get("DF_DB_MONGO_URI", "")
                               + "-----"
                               + os.environ.get("DF_DB_MONGO_NAME", ""))
            print("Config", self.storage)
