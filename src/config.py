"""
A module for configuring the project.
"""
import os


class Config:
    """A class for configuring the project.

    :param config_file: Path to config.yaml file.
    :returns: Void (creates config instance)
    """

    def __init__(self, config_file):
        # import here (not at top of file) to avoid circular imports
        from .utils import yaml_load

        with open(config_file, "r") as f:
            config = yaml_load(f)

        self.DATA_PATH = config["paths"]["data_path"]
        self.LOG_PATH = config["logging"]["file_path"]
        self.SPATIAL_REFERENCE = config["spatial_reference"]["utm33"]


# load .env config.yaml file from project root
PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir)
config_file = os.path.join(PROJECT_DIR, "config.yaml")

config_instance = Config(config_file)


if __name__ == "__main__":
    PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir)
    config_file = os.path.join(PROJECT_DIR, "config.yaml")
    config_instance = Config(config_file)

    print(config_instance.DATA_PATH)
