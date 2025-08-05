import yaml
from box.exceptions import BoxValueError
import os
from pathlib import Path
from typing import Any
from box import ConfigBox
import pickle

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return ConfigBox(content)

def create_directories(paths: list, verbose: bool = True):
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            print(f"Directory created at: {path}")
            
import os
import pickle

def save_object(file_path: str, obj: object) -> None:
    # Ensure directory exists
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)

    # Save the object
    with open(file_path, "wb") as file_obj:
        pickle.dump(obj, file_obj)
