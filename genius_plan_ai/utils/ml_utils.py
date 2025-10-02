# Genius_plan_ai/utils/ml_utils.py
import joblib
import pandas as pd
from genius_plan_ai.config import ML_MODEL_PATH
import streamlit as st

def load_ml_model():
    try:
        model = joblib.load(ML_MODEL_PATH)
        return model
    except Exception:
        return None

def predict_session_duration(model, subject_name, priority, default_duration):
    """
    model.predict expects a DataFrame with columns the model was trained on,
    but fallback to default_duration if anything fails.
    """
    if model is None:
        return default_duration
    try:
        df = pd.DataFrame([{"Subject": subject_name, "Priority": priority}])
        pred = model.predict(df)[0]
        return max(15, int(pred))
    except Exception as e:
        st.warning(f"Prediction failed: {e}")
        return default_duration
