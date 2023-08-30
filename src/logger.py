"""
A module for logging configuration.
"""

import datetime
import logging
import os
import sys

# local imports
from .utils import yaml_load

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
config_file = os.path.join(project_dir, "config.yaml")

LOGGER = logging.getLogger(__name__)


def setup_logger(logfile=False):
    """Setup logging configuration.

    :param logfile: If True, log to file. Otherwise, log to console. (Default value = False)
    :returns: Void (creates logging instance)

    """

    # load logging configuration from config.yaml
    with open(config_file, "r") as f:
        config = yaml_load(f)
        log_level = config["logging"]["level"]
        log_format = config["logging"]["log_format"]
        date_format = config["logging"]["date_format"]
        date_format_os = config["logging"]["date_format_os"]
        file_path = config["logging"]["file_path"]

    # Remove all existing handlers from the logger
    for handler in LOGGER.handlers:
        LOGGER.removeHandler(handler)

    log_file_name = (
        datetime.datetime.now().strftime(date_format_os)
        + "_"
        + os.path.splitext(os.path.basename(sys.argv[0]))[0]
        + ".log"
    )
    log_file_path = os.path.join(file_path, log_file_name)

    if logfile:
        # set file handler
        logging.basicConfig(
            level=log_level,
            datefmt=date_format,
            format=log_format,
            filename=log_file_path,
        )

    else:
        # set consoler handler
        logging.basicConfig(
            level=log_level, datefmt=date_format, format=log_format, stream=sys.stdout
        )

    LOGGER.debug("Logging initialized")
    return


if __name__ == "__main__":
    setup_logger(logfile=False)
    LOGGER.info("Information message")
