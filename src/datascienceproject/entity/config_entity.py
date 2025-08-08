from dataclasses import dataclass
from typing import Dict

# -------------------- Data Ingestion Config --------------------
@dataclass
class DataIngestionConfig:
    root_dir: str
    source_url: str
    local_data_file: str

# -------------------- Data Validation Config --------------------
@dataclass
class DataValidationConfig:
    root_dir: str
    data_path: str                  # Points to raw data (ingestion output)
    validated_data_path: str       # Points to the cleaned/validated CSV
    STATUS_FILE: str
    all_schema: Dict               # Your schema to validate columns

# -------------------- Data Transformation Config --------------------
@dataclass
class DataTransformationConfig:
    validated_data_path: str       # Input to transformation
    transformed_data_path: str     # Output path for transformed data


# src/datascienceproject/entity/config_entity.py



@dataclass
class ModelTrainerConfig:
    transformed_data_path: str
    model_path: str
    target_column: str
