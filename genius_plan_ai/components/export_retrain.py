
import streamlit as st
import pandas as pd
import os
from genius_plan_ai.config import LOG_FILE, ML_MODEL_PATH
from genius_plan_ai.train_model import train_and_save_model

def render_export_retrain():
    st.header("💾 Export & Retrain")
    plan = st.session_state.get("study_plan_df")
    if plan is not None and not plan.empty:
        csv = plan.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Plan (CSV)", csv, "genius_plan_plan.csv", "text/csv")
    else:
        st.info("No plan to export.")

    if os.path.exists(LOG_FILE):
        log_csv = open(LOG_FILE, "rb").read()
        st.download_button("📈 Download Log (CSV)", log_csv, "study_log.csv", "text/csv")
    else:
        st.info("No study log yet.")

    if st.button("🔁 Retrain Adaptive Model"):
        with st.spinner("Retraining..."):
            path = train_and_save_model()
            st.success(f"Model retrained and saved to {path}")
