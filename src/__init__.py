"""
py-linux-template
=================

A template packagee for Python projects on Linux.
"""

__author__ = "Willeke A'Campo"
__email__ = "willeke.acampo@nina.no"
__version__ = "0.1.0"

# import config global variables

from .logger import setup_logger  # noqa
from .config import PROJECT_DIR, LOG_PATH, DATA_PATH, SPATIAL_REFERENCE  # noqa
