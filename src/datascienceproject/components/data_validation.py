import pandas as pd
import os
from src.datascienceproject.components.data_ingestion import DataIngestion
from src.datascienceproject.entity.config_entity import DataValidationConfig 
from src.datascienceproject import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            
            data = pd.read_csv(self.config.unzip_data_path)

            
            expected_columns = list(self.config.all_schema.keys())
            actual_columns = list(data.columns)

            logger.info(f"Expected columns: {expected_columns}")
            logger.info(f"Actual columns: {actual_columns}")

            if expected_columns != actual_columns:
                logger.warning("Column mismatch found!")
                validation_status = False

            return validation_status

        except Exception as e:
            logger.error(f"Exception occurred during data validation: {e}")
            raise e
