import pandas as pd
from src.datascienceproject.components.predictor import Predictor
import os

class PredictionPipeline:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model", "model.pkl")
        self.sample_input_path = os.path.join("artifacts", "prediction_input", "new_data.csv")

    def run(self):
        predictor = Predictor(model_path=self.model_path)

        # Load new input data
        input_df = pd.read_csv(self.sample_input_path)

        # Make predictions
        preds = predictor.predict(input_df)

        # Save predictions
        output_path = os.path.join("artifacts", "prediction_output", "predictions.csv")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pd.DataFrame({"Prediction": preds}).to_csv(output_path, index=False)
        print(f"✅ Predictions saved to {output_path}")
