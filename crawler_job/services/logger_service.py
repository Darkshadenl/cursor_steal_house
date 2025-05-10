import logging
import os
from colorlog import ColoredFormatter


def setup_logger(name: str) -> logging.Logger:
    formatter = ColoredFormatter(
        "%(log_color)s[%(levelname)s]%(reset)s %(cyan)s%(name)s:%(reset)s %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    debug_mode = os.getenv("DEBUG_MODE", "false").lower() == "true"
    if debug_mode:
        log_level = "DEBUG"
    logger.setLevel(log_level)
    logger.handlers.clear()
    logger.addHandler(handler)

    return logger
