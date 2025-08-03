from src.datascienceproject.constants import *
from src.datascienceproject.utils.common import read_yaml
from src.datascienceproject.entity.config_entity import (
    DataValidationConfig,
    DataIngestionConfig
)
import os


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, schema_file_path=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)

        os.makedirs(self.config["data_ingestion"]["root_dir"], exist_ok=True)
        os.makedirs(self.config["data_validation"]["root_dir"], exist_ok=True)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]

        return DataIngestionConfig(
            root_dir=config["root_dir"],
            source_url=config["source_URL"],
            local_data_file=config["local_data_file"],
            unzip_dir=None  # since you're not using zip anymore
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config["data_validation"]
        schema = self.schema["COLUMNS"]

        return DataValidationConfig(
            root_dir=config["root_dir"],
            local_data_file=config["local_data_file"],
            all_schema=schema,
            STATUS_FILE=config["STATUS_FILE"]
        )
