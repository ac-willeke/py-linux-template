"""
py-linux-template
=================

A template packagee for Python projects on Linux.
"""

__author__ = "Willeke A'Campo"
__email__ = "willeke.acampo@nina.no"
__version__ = "0.1.0"

# import config global variables

from .config import DATA_PATH, LOG_PATH, PROJECT_DIR, SPATIAL_REFERENCE  # noqa
from .logger import setup_logger  # noqa
