from dataclasses import dataclass
from typing import Dict


@dataclass
class DataIngestionConfig:
    root_dir: str
    source_url: str
    local_data_file: str


@dataclass
class DataValidationConfig:
    root_dir: str
    local_data_file: str
    all_schema: dict
    STATUS_FILE: str
