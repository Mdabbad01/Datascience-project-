from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_transformation import DataTransformation
from src.datascienceproject import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            logger.info(">>>>>> stage Data Transformation started <<<<<<")

            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.transform_data()

            logger.info(">>>>>> stage Data Transformation completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(f"Error in Data Transformation Pipeline: {e}")
            raise e
