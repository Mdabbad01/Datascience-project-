from src.datascienceproject import logger 
from src.datascienceproject.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascienceproject.constants import CONFIG_FILE_PATH
from src.datascienceproject.utils.common import read_yaml, create_directories



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e