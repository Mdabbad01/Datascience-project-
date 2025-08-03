
import os
import zipfile
import urllib.request
from src.datascienceproject.entity.config_entity import DataIngestionConfig
from src.datascienceproject import logger  # if you have a logger setup


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

    def extract_zip_file(self):
        if self.config.unzip_dir:
            os.makedirs(self.config.unzip_dir, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
                logger.info(f"Data extracted to: {self.config.unzip_dir}")
        else:
            logger.info("Skipping extraction as unzip_dir is not set.")
