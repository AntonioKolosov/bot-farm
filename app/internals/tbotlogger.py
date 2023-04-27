"""
"""


import logging
import sys


class TBotLogger:
    def __init__(self,
                 level: int = logging.INFO,
                 log_path: str = "logs/twbot.log") -> None:
        """"""
        logging.basicConfig(level=level,
                            format="%(asctime)s %(levelname)s %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            filename=log_path)

    def log_info(self, message: str) -> None:
        file = sys._getframe(1).f_code.co_filename
        func = sys._getframe(1).f_code.co_name
        line = sys._getframe(1).f_code.co_firstlineno
        logging.info(f"{file} {line} {func} {message}")


tb_log = TBotLogger()
