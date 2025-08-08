import pandas as pd
from src.datascienceproject.entity.config_entity import DataTransformationConfig
from src.datascienceproject import logger
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_data(self):
        try:
            df = pd.read_csv(self.config.validated_data_path)

            # Sample transformation: drop missing values
            df = df.dropna()

            # Sample: convert categorical to numeric (you can customize this)
            for col in df.select_dtypes(include='object').columns:
                df[col] = df[col].astype('category').cat.codes

            os.makedirs(os.path.dirname(self.config.transformed_data_path), exist_ok=True)
            df.to_csv(self.config.transformed_data_path, index=False)
            logger.info(f"Data transformed and saved at {self.config.transformed_data_path}")

        except Exception as e:
            logger.error(f"Error in data transformation: {e}")
            raise e
