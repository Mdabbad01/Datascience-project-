from src.datascienceproject.components.model_evaluation import ModelEvaluation
import os

class ModelEvaluationPipeline:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model", "model.pkl")
        self.test_data_path = os.path.join("artifacts", "data_transformation", "transformed_iris.csv")

    def run(self):
        evaluator = ModelEvaluation(
            model_path=self.model_path,
            test_data_path=self.test_data_path
        )
        evaluator.evaluate()
