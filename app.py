import streamlit as st
import pandas as pd
from src.datascienceproject.pipeline.prediction_pipeline import PredictionPipeline

st.set_page_config(page_title="ML Predictor", layout="centered")

st.title("🚀 Machine Learning Predictor App")
st.write("Upload a CSV file with input data to get predictions.")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    st.write("✅ Uploaded Data Preview:")
    st.dataframe(input_df)

    # Save to temp path
    sample_input_path = "artifacts/prediction_input/new_data.csv"
    input_df.to_csv(sample_input_path, index=False)

    # Run prediction pipeline
    predictor = PredictionPipeline()
    try:
        predictor.run()
        output_path = "artifacts/prediction_output/predictions.csv"
        predictions = pd.read_csv(output_path)
        st.success("🎉 Predictions Generated Successfully!")
        st.write(predictions)
    except Exception as e:
        st.error(f"❌ Error while predicting: {str(e)}")
