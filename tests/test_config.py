"""
Test Module for utils.py
"""

import pytest

# Import the module you want to test
from src.config import Config

from .utils import get_test_file_path


@pytest.fixture()
def path_to_config_file():
    """path to config.yaml file"""
    test_config_file = get_test_file_path("test_config.yaml")
    return test_config_file


def test_config(path_to_config_file):
    """test config.py

    :param path_to_config_file:
    """
    config_instance = Config(path_to_config_file)
    assert config_instance.DATA_PATH == "/path/to/data"
    assert config_instance.LOG_PATH == "/path/to/log"
