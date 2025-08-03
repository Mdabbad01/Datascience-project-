
import os
import urllib.request
from src.datascienceproject.entity.config_entity import DataIngestionConfig
from src.datascienceproject import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urllib.request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! Info: \n{headers}")
        else:
            logger.info(f"File already exists at: {self.config.local_data_file}")
