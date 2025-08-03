from src.datascienceproject.constants import *
from src.datascienceproject.utils.common import read_yaml
from src.datascienceproject.entity.config_entity import DataValidationConfig
import os

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, schema_file_path=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)
        os.makedirs(self.config.data_validation.root_dir, exist_ok=True)

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        return DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_path=config.unzip_data_path,
            all_schema=schema
        )
