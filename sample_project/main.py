"""
Main Script

This script servers as the entry point
for the sub-packages and modules of the project.
"""

import logging
import sys
from pathlib import Path

# Add the root directory of the project to the Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src import DATA_PATH, LOG_PATH, PROJECT_DIR, SPATIAL_REFERENCE  # noqa
from src.logger import setup_logger  # noqa


def main():
    """Run administrative tasks."""

    # Log a debug message
    logging.debug("Starting main function...")

    # Access settings variables
    logging.info("PROJECT_DIR: %s", PROJECT_DIR)
    logging.info("LOG_PATH: %s", LOG_PATH)
    logging.info("DATA_PATH: %s", DATA_PATH)
    logging.info("SPATIAL_REFERENCE: %s", SPATIAL_REFERENCE)

    # Log an info message
    logging.info("Accessed settings variables")

    # Rest of your code...


if __name__ == "__main__":
    setup_logger(logfile=True)  #
    main()
