"""
Simple logger with pure Python
"""

import logging
import sys

from ..config import cfg

log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
    "FATAL": logging.FATAL
}


class TBotLogger:
    def __init__(self) -> None:
        """Setup logger parametres"""
        log_level = cfg.log_level
        # log_path = cfg.log_path  # ignoreqa F841
        log_level = log_levels.get(log_level, logging.WARNING)
        logging.basicConfig(level=log_level,
                            format="%(asctime)s %(levelname)s %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            handlers=[logging.StreamHandler(sys.stdout)])

    def log_info(self, message: str) -> None:
        file = sys._getframe(1).f_code.co_filename
        func = sys._getframe(1).f_code.co_name
        line = sys._getframe(1).f_code.co_firstlineno
        logging.info(f"{file} {line} {func} {message}")


tb_log = TBotLogger()
