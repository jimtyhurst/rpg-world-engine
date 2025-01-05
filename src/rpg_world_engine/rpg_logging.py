import logging
import sys
import time

LOG_FORMAT = "{asctime} UTC;{levelname};{name};{funcName};{message}"
LOG_FORMATTER = logging.Formatter(LOG_FORMAT, style="{")
LOG_FORMATTER.converter = time.gmtime
RPG_LOG_FILE_NAME = "rpg.log"
FILE_LOG_HANDLER = logging.FileHandler(
    RPG_LOG_FILE_NAME,
    mode="a",
    encoding="utf-8",
)
FILE_LOG_HANDLER.setFormatter(LOG_FORMATTER)
CONSOLE_LOG_HANDLER = logging.StreamHandler(sys.stdout)
CONSOLE_LOG_HANDLER.setFormatter(LOG_FORMATTER)
logging.basicConfig(
    format=LOG_FORMAT,
    style="{",
    handlers=[CONSOLE_LOG_HANDLER, FILE_LOG_HANDLER],
    level=logging.WARNING,
)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
