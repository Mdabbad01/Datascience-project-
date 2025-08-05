import pickle
import pandas as pd
import os

class Predictor:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        with open(self.model_path, "rb") as f:
            return pickle.load(f)

    def predict(self, input_data: pd.DataFrame):
        predictions = self.model.predict(input_data)
        return predictions
