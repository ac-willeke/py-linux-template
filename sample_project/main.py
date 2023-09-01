"""
Main Script

This script servers as the entry point
for the sub-packages and modules of the project.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# setup logging
from src.logger import reset_logger, setup_custom_logger, setup_logger  # noqa

# LOGGER = logging.getLogger(__name__)


def main():
    """example main function"""

    # log project configuration
    logger = setup_logger("staging")
    logger.info("test info")

    reset_logger()
    custom_logger = setup_custom_logger(logfile=True)
    custom_logger.debug("test info 2")


if __name__ == "__main__":
    main()
