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


def setup_logging(
    default_path="config/config_logging.yaml",
    default_level=logging.INFO,
):
    """Setup logging configuration

    :param default_path:  (Default value = 'config/config_logging.yaml')
    :param default_level:  (Default value = logging.INFO)

    """
    path = default_path
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def setup_custom_logging(
    config_path="config/config_logging.yaml", logfile=True, logpath=None
):
    """Setup logging configuration.
    The custom logger enables dynamic logfile names.

    :param logfile: If True, log to file. Otherwise, log to console. (Default value = False)
    :param logpath: The path to the log file if `logfile` is True. (Default value = None)
    :param config_path:  (Default value = 'config/config_logging.yaml')
    :returns: Void (creates logging instance)

    """

    # import local modules within function to avoid circular imports
    try:
        # module use
        from src.utils import yaml_load
        from src import PROJECT_DIR
    except ModuleNotFoundError:
        # standalone use of logger.py
        from utils import yaml_load
        from config import PROJECT_DIR

    # load logging configuration
    with open(config_path, "r") as f:
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


## Example usage of logger within modules
def test_function():
    """Test function for logging"""

    logger = logging.getLogger(__name__)
    logger.info("This is a information message.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is a error message.")
    logger.critical("This is a critical message.")
    return


class Test(object):
    """Test class for logging.

    :Methods:
        - :log_config: Log project configuration
        - :log_best_practices: Log best practices
    """

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def log_config(self):
        """Log project configuration"""
        try:
            # loaded as module
            from src.config import DATA_PATH, PROJECT_DIR, SPATIAL_REFERENCE  # noqa
        except ModuleNotFoundError:
            # standalone use of logger.py
            from config import DATA_PATH, PROJECT_DIR, SPATIAL_REFERENCE  # noqa

        self.logger.info("Log project configuration:")

        # Access configuration variables
        self.logger.info("PROJECT_DIR: %s", PROJECT_DIR)
        self.logger.info("DATA_PATH: %s", DATA_PATH)
        self.logger.info("SPATIAL_REFERENCE: %s", SPATIAL_REFERENCE)
        self.logger.info("Project configuration logged.")

    def log_best_practices(self):
        """Log best practices"""
        self.logger.info("Logging best practices:")
        self.logger.info("Use __name__ as the logger name.")
        self.logger.info(
            "Do not use logger at module level,\n\
            get logger within functions or classes instead.\n\
            Otherwise, the logger will be initialized when the module is imported,\n\
            this is often before the logging configuration is set up."
        )
        self.logger.info("Best practices logged.")


if __name__ == "__main__":

    # setup loggging for standalone use of logger.py
    setup_logging()
    logger = logging.getLogger(__name__)

    # test project logger
    Test(logger).log_config()
    Test(logger).log_best_practices()

    # test custom logger
    reset_logger()
    custom_logger = setup_custom_logging(logfile=True)
    test_function()

    pass
