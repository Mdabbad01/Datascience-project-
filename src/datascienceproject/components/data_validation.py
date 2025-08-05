import pandas as pd
import os
from src.datascienceproject.entity.config_entity import DataValidationConfig 
from src.datascienceproject import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            # ✅ Load the ingested file from data_ingestion
            data = pd.read_csv(self.config.data_path)

            expected_columns = list(self.config.all_schema.keys())
            actual_columns = list(data.columns)

            logger.info(f"Expected columns: {expected_columns}")
            logger.info(f"Actual columns: {actual_columns}")

            if expected_columns != actual_columns:
                logger.warning("Column mismatch found!")
                validation_status = False
            else:
                # ✅ Save the validated data to data_validation
                os.makedirs(os.path.dirname(self.config.validated_data_path), exist_ok=True)
                data.to_csv(self.config.validated_data_path, index=False)
                logger.info(f"Validated data saved at: {self.config.validated_data_path}")

            # ✅ Write the status to status file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.error(f"Exception occurred during data validation: {e}")
            raise e
