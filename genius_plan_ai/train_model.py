# genius_plan_ai/train_model.py

import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from genius_plan_ai.config import LOG_FILE, ML_MODEL_PATH
import numpy as np


# --- FIX: put this at module level (not inside function) ---
class ConstantModel:
    """Fallback model that always predicts a constant duration."""
    def __init__(self, const=45):
        self.const = const
    def predict(self, X):
        n = len(X)
        return np.array([self.const] * n)


def train_and_save_model():
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        if {'Subject', 'Priority', 'Actual_Duration'}.issubset(df.columns) and not df.empty:
            X = df[['Subject', 'Priority']].copy()
            y = df['Actual_Duration'].astype(float).values

            preprocessor = ColumnTransformer(
                transformers=[
                    ('subj', OneHotEncoder(handle_unknown='ignore'), ['Subject']),
                ],
                remainder='passthrough'
            )

            model = Pipeline(steps=[
                ('pre', preprocessor),
                ('rf', RandomForestRegressor(n_estimators=50, random_state=42))
            ])

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model.fit(X_train, y_train)

            os.makedirs(os.path.dirname(ML_MODEL_PATH), exist_ok=True)
            joblib.dump(model, ML_MODEL_PATH)
            return ML_MODEL_PATH

    # fallback model
    fallback = ConstantModel(const=45)
    os.makedirs(os.path.dirname(ML_MODEL_PATH), exist_ok=True)
    joblib.dump(fallback, ML_MODEL_PATH)
    return ML_MODEL_PATH


if __name__ == "__main__":
    path = train_and_save_model()
    print(f"Saved model to: {path}")
