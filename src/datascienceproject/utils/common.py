import yaml
import os
from pathlib import Path
from typing import Any


def read_yaml(path_to_yaml: Path) -> Any:
    with open(path_to_yaml, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content


def create_directories(paths: list):
    for path in paths:
        os.makedirs(path, exist_ok=True)
