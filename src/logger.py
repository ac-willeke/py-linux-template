import datetime
import logging
import logging.config
import os
import sys
import yaml

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
config_file = os.path.join(project_dir, "config/config_logger.yaml")


def reset_logger():
    """Reset the logger configuration to default."""
    logging.shutdown()
    logging.root.handlers = []  # Remove all handlers
    logging.root.setLevel(logging.WARNING)  # Set the root logger to a default level
    return


def setup_logger(logger_object=__name__):
    """Setup logging configuration according to config_logger.yaml file

    :param logger_object: "dev", "staging", "prod" (Default value = __name__)
    :returns: The logger object
    """
    with open(config_file, "r") as f:
        config = yaml.safe_load(f.read())

    logging.config.dictConfig(config)
    logger = logging.getLogger(logger_object)
    logger.debug("Logging initialized")

    return logger


def setup_custom_logger(logfile=True, logpath=None):
    """Setup logging configuration according to config_logger.yamle file.
    The custom logger enables dynamic logfile names.

    :param logfile: If True, log to file. Otherwise, log to console. (Default value = False)
    :param logpath: The path to the log file if `logfile` is True. (Default value = None)
    :returns: Void (creates logging instance)
    """

    # import local modules within function to avoid circular imports
    from src import PROJECT_DIR
    from src.utils import yaml_load

    # load logging configuration
    with open(config_file, "r") as f:
        config = yaml_load(f)

    log_level = config["handlers"]["console"]["level"]
    log_format = config["formatters"]["simple"]["format"]
    date_format = config["formatters"]["simple"]["datefmt"]
    if logpath is None:
        logpath = os.path.join(PROJECT_DIR, "log")
    else:
        logpath = logpath

    logfile_name = (
        datetime.datetime.now().strftime(date_format)
        + "_"
        + os.path.splitext(os.path.basename(sys.argv[0]))[0]
        + ".log"
    )
    path = os.path.join(logpath, logfile_name)

    if logfile:
        logging.basicConfig(
            level=log_level,
            datefmt=date_format,
            format=log_format,
            filename=path,
        )
    else:
        logging.basicConfig(
            level=log_level, datefmt=date_format, format=log_format, stream=sys.stdout
        )
    logger = logging.getLogger(__name__)
    logger.debug("Logging initialized")

    return logger


def start_logger():
    """Start the logger if the script is run directly."""
    LOGGER = setup_custom_logger(logfile=False)

    # import local modules within function to avoid circular imports
    from src.config import DATA_PATH, LOG_PATH, PROJECT_DIR, SPATIAL_REFERENCE  # noqa

    # Access configuration variables
    LOGGER.info("PROJECT_DIR: %s", PROJECT_DIR)
    LOGGER.info("LOG_PATH: %s", LOG_PATH)
    LOGGER.info("DATA_PATH: %s", DATA_PATH)
    LOGGER.info("SPATIAL_REFERENCE: %s", SPATIAL_REFERENCE)
    LOGGER.info("Accessed settings variables")

    return


if __name__ == "__main__":
    # local imports loaded as module, do not run as standalone script.
    pass
