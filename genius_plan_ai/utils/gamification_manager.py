# Genius_plan_ai/utils/gamification_manager.py
import streamlit as st
import pandas as pd
from datetime import datetime
import os
from genius_plan_ai.config import LOG_FILE, ACHIEVEMENTS_MAP

def initialize_gamification():
    defaults = {
        "study_streak": 0,
        "total_sessions_completed": 0,
        "achievements": [],
        "last_study_date": None
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def log_completion_event(task_details, priority_level):
    # task_details: dict with Date, Day, Start Time, Details, Actual Duration (min)
    record = {
        "completion_timestamp": datetime.now().isoformat(),
        "Date": task_details.get("Date"),
        "Day": task_details.get("Day"),
        "Start_Time": task_details.get("Start Time"),
        "Details": task_details.get("Details"),
        "Subject": task_details.get("Details").split(" - ")[0] if task_details.get("Details") else "",
        "Priority": priority_level,
        "Actual_Duration": task_details.get("Actual Duration (min)", 0)
    }
    df = pd.DataFrame([record])
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    df.to_csv(LOG_FILE, mode='a', header=not os.path.exists(LOG_FILE), index=False)
    st.success("Completion logged ✅")

def update_gamification(plan_df):
    if plan_df is None or plan_df.empty:
        return
    study_tasks = plan_df[plan_df["Activity"] == "Study 📖"]
    completed = study_tasks[study_tasks["Status"] == True]
    st.session_state.total_sessions_completed = int(len(completed))
    if not completed.empty:
        last_date = pd.to_datetime(completed["Date"]).max().date()
        if st.session_state.last_study_date is None:
            st.session_state.study_streak = 1
        else:
            delta = (last_date - st.session_state.last_study_date).days
            if delta == 1:
                st.session_state.study_streak += 1
            elif delta > 1:
                st.session_state.study_streak = 1
        st.session_state.last_study_date = last_date
    check_achievements()

def check_achievements():
    for name, cond in ACHIEVEMENTS_MAP.items():
        try:
            if cond(st.session_state) and name not in st.session_state.achievements:
                st.session_state.achievements.append(name)
                st.toast(f"🎉 Achievement unlocked: {name}!")
        except Exception:
            pass
