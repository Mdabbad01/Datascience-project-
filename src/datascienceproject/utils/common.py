import yaml
from box.exceptions import BoxValueError
import os
from pathlib import Path
from typing import Any
from box import ConfigBox

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return ConfigBox(content)

def create_directories(paths: list, verbose: bool = True):
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            print(f"Directory created at: {path}")
