# src/datascienceproject/pipeline/model_trainer_pipeline.py

from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.model_trainer import ModelTrainer
from src.datascienceproject import logger

STAGE_NAME = "Model Training"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager().get_model_trainer_config()
        trainer = ModelTrainer(config)
        trainer.train_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.run()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
