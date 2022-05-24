import argparse
import logging
from typing import Literal

# set color logger
mapping = {
    "TRACE": "[ trace ]",
    "DEBUG": "[ \x1b[0;36mdebug\x1b[0m ]",
    "INFO": "[ \x1b[0;32minfo\x1b[0m ]",
    "WARNING": "[ \x1b[0;33mwarn\x1b[0m ]",
    "WARN": "[ \x1b[0;33mwarn\x1b[0m ]",
    "ERROR": "\x1b[0;31m[ error ]\x1b[0m",
    "ALERT": "\x1b[0;37;41m[ alert ]\x1b[0m",
    "CRITICAL": "\x1b[0;37;41m[ alert ]\x1b[0m",
}


class ColorfulHandler(logging.StreamHandler):
    def emit(self, record):
        record.levelname = mapping[record.levelname]
        super().emit(record)


LogLevel = Literal["error", "warning", "warn", "info", "debug"]


def _set_loglevel(level: LogLevel):
    if level == "error":
        return logging.ERROR
    elif level == "warning":
        return logging.WARNING
    elif level == "warn":
        return logging.WARN
    elif level == "info":
        return logging.INFO
    else:
        return logging.DEBUG


def set_loglevel(level: LogLevel):
    level = _set_loglevel(level)
    logging.basicConfig(handlers=[ColorfulHandler()], level=level)


def set_loglevel_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """add `loglevel` args to parser
    Args:
        parser (argparse.ArgumentParser): parser
    Returns:
        argparse.ArgumentParser: parser added loglevel
    """
    parser.add_argument(
        "--loglevel",
        default="info",
        choices=["error", "warning", "warn", "info", "debug"],
        help="set log level",
    )

    return parser
