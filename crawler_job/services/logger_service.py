import logging
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
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.addHandler(handler)

    return logger
