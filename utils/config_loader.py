import yaml
from pathlib import Path

def load_config(config_path="config/config.yaml"):
    """
    Loads the YAML configuration file.

    :param config_path: Optional path to the config file.
    :return: Dictionary containing configuration values.
    """

    with open(config_path, "r") as f:
        return yaml.safe_load(f) 