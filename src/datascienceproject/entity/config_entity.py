from dataclasses import dataclass
from pathlib import Path
from typing import Dict

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_path: Path
    all_schema: Dict



@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    all_schema: dict
    STATUS_FILE: Path