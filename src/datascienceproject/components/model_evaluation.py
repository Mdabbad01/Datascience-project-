import pandas as pd
import pickle
import os
from sklearn.metrics import accuracy_score

class ModelEvaluation:
    def __init__(self, model_path, test_data_path):
        self.model_path = model_path
        self.test_data_path = test_data_path

    def load_model(self):
        with open(self.model_path, "rb") as f:
            return pickle.load(f)

    def evaluate(self):
        # Load model and data
        model = self.load_model()
        df = pd.read_csv(self.test_data_path)

        # Assume last column is target
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        # Predict and evaluate
        y_pred = model.predict(X)
        acc = accuracy_score(y, y_pred)
        print(f"\n✅ Model Accuracy: {acc:.4f}")
        return acc
