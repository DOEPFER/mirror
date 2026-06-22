import logging
import secrets
import sys
import time
from datetime import datetime, timezone
from logging import Logger
from pathlib import Path


def setup_logging(logprefix: str = "mirror", verbose: bool = False) -> Logger:
    """
    Set up the logging configuration.

    Args:
        logprefix (str): Prefix for the log file name. Defaults to 'mirror'.
        verbose (bool): If True, logs are also printed to the standard output. Defaults to False.

    Returns:
        Logger: The configured logger instance.
    """
    log_dir = Path("log")
    log_dir.mkdir(parents=True, exist_ok=True)

    date = datetime.now(timezone.utc)
    short_hash = secrets.token_hex(4)
    log_filename = f"{logprefix}_{date:%Y_%m_%d_%H_%M_%S}_{short_hash}.log"
    log_file_path = log_dir / log_filename

    handlers = (
        [
            logging.FileHandler(log_file_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ]
        if verbose
        else [logging.FileHandler(log_file_path, encoding="utf-8")]
    )

    logging.Formatter.converter = time.gmtime  # UTC

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)sZ | %(levelname)s | [%(name)s] | %(message)s",
        handlers=handlers,  # type: ignore
        datefmt="%Y-%m-%dT%H:%M:%S",  # ISO 8601
    )

    return logging.getLogger("mirror")
