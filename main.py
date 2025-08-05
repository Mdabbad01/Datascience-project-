from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascienceproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascienceproject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

from src.datascienceproject.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascienceproject.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.datascienceproject.pipeline.prediction_pipeline import PredictionPipeline
from src.datascienceproject.pipeline.model_trainer_pipeline import ModelTrainerPipeline
import mlflow

from src.datascienceproject import logger

# Stage 1: Data Ingestion
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    ingestion = DataIngestionTrainingPipeline()
    ingestion.initiate_data_ingestion()  # ✅ Correct method name
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 2: Data Validation
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    validation = DataValidationTrainingPipeline()
    validation.initiate_data_validation()  # ✅ Correct method name
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 3: Data Transformation
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    transformation = DataTransformationTrainingPipeline()
    transformation.run()  # ✅ Correct method name
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



if __name__ == "__main__":
    try:
        logger.info(">>>>>> Model Trainer Stage started <<<<<<")
        trainer = ModelTrainerPipeline()
        trainer.run()
        logger.info(">>>>>> Model Trainer Stage completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    try:
        ...
        print("\n" + "x==========x")
        print(">>>>> Model Evaluation Stage started <<<<<")
        evaluator = ModelEvaluationPipeline()
        evaluator.run()
        print(">>>>> Model Evaluation Stage completed <<<<<")
        print("x==========x\n")

    except Exception as e:
        raise e

if __name__ == "__main__":
    try:
        ...
        print("\n" + "x==========x")
        print(">>>>> Prediction Stage started <<<<<")
        predictor = PredictionPipeline()
        predictor.run()
        print(">>>>> Prediction Stage completed <<<<<")
        print("x==========x\n")
    except Exception as e:
        raise e
    
    
    mlflow.set_tracking_uri("file:///C:/Users/hr591/OneDrive/Desktop/DatascienceProject/mlruns")

# Start training
pipeline = ModelTrainerPipeline()
pipeline.run()