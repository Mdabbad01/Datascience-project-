# src/datascienceproject/components/model_trainer.py

import os
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from src.datascienceproject import logger
from src.datascienceproject.utils.common import save_object
from src.datascienceproject.entity.config_entity import ModelTrainerConfig
import mlflow
import mlflow.sklearn

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        data = pd.read_csv(self.config.transformed_data_path)
        X = data.drop(self.config.target_column, axis=1)
        y = data[self.config.target_column]

        # Set MLflow Tracking URI and experiment name
        mlflow.set_tracking_uri("file:///absolute/path/to/your/project/mlruns")  # 👈 Use your real path
        mlflow.set_experiment("Model_Training_Experiment")

        with mlflow.start_run(run_name="LogisticRegressionModel"):
            model = LogisticRegression()
            model.fit(X, y)

            # Save model
            save_object(self.config.model_path, model)

            # Evaluate and log accuracy
            y_pred = model.predict(X)
            acc = accuracy_score(y, y_pred)

            logger.info(f"Training accuracy: {acc}")
            print(f"Training accuracy: {acc}")

            # Log parameters, metrics, and model
            mlflow.log_param("model_type", "LogisticRegression")
            mlflow.log_metric("accuracy", acc)
            mlflow.sklearn.log_model(model, "model")

            # Optional: log config file or path as artifact
            mlflow.log_artifact(self.config.transformed_data_path)
import os
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from src.datascienceproject import logger
from src.datascienceproject.utils.common import save_object
from src.datascienceproject.entity.config_entity import ModelTrainerConfig
import mlflow
import mlflow.sklearn

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        data = pd.read_csv(self.config.transformed_data_path)
        X = data.drop(self.config.target_column, axis=1)
        y = data[self.config.target_column]

        # Set MLflow Tracking URI and experiment name
        mlflow.set_tracking_uri("file:///absolute/path/to/your/project/mlruns")  # 👈 Use your real path
        mlflow.set_experiment("Model_Training_Experiment")

        with mlflow.start_run(run_name="LogisticRegressionModel"):
            model = LogisticRegression()
            model.fit(X, y)

            # Save model
            save_object(self.config.model_path, model)

            # Evaluate and log accuracy
            y_pred = model.predict(X)
            acc = accuracy_score(y, y_pred)

            logger.info(f"Training accuracy: {acc}")
            print(f"Training accuracy: {acc}")

            # Log parameters, metrics, and model
            mlflow.log_param("model_type", "LogisticRegression")
            mlflow.log_metric("accuracy", acc)
            mlflow.sklearn.log_model(model, "model")

            # Optional: log config file or path as artifact
            mlflow.log_artifact(self.config.transformed_data_path)
