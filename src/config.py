"""
A module for configuring the project.
"""
import os


class Config:
    """
    A class for configuring the project.

    Parameters
    ----------
    config_file : str
        Path to config.yaml file.

    Returns
    -------
    type
        Void (creates config instance)

    """

    def __init__(self, config_file):
        # local imports
        try:
            from src.utils import yaml_load
        except ModuleNotFoundError:
            from utils import yaml_load

        with open(config_file, "r") as f:
            config = yaml_load(f)

        self.DATA_PATH = config["paths"]["data_path"]
        self.SPATIAL_REFERENCE = config["spatial_reference"]["utm33"]
        return


# global variables
PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir)
CONFIG_FILE = os.path.join(PROJECT_DIR, "config/config.yaml")

# create config instance and load global variables
config_instance = Config(CONFIG_FILE)
DATA_PATH = config_instance.DATA_PATH
SPATIAL_REFERENCE = config_instance.SPATIAL_REFERENCE


def main():
    print("Testing config.py...")
    print(f"PROJECT_DIR: {PROJECT_DIR}")
    print(f"CONFIG_FILE: {CONFIG_FILE}")
    print(f"DATA_PATH: {DATA_PATH}")
    print(f"SPATIAL_REFERENCE: {SPATIAL_REFERENCE}")


if __name__ == "__main__":
    main()
