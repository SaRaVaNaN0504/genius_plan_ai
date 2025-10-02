# Genius_plan_ai/components/main_dashboard.py
import streamlit as st
import pandas as pd
from genius_plan_ai.utils.gamification_manager import log_completion_event, update_gamification, initialize_gamification

def render_main_dashboard():
    initialize_gamification()
    st.header("📊 Main Dashboard")

    if "study_plan_df" not in st.session_state or st.session_state.study_plan_df is None or st.session_state.study_plan_df.empty:
        st.info("No plan generated yet. Use the sidebar to build a plan.")
        return

    plan = st.session_state.study_plan_df.copy()
    st.markdown("### 🗂️ Schedule")

    try:
        edited = st.data_editor(
            plan,
            column_config={
                "Status": st.column_config.CheckboxColumn("✅ Done?"),
                "Details": st.column_config.TextColumn("📖 Topic", width="large"),
                "Actual Duration (min)": st.column_config.NumberColumn("Actual Time (min)", min_value=0, step=5)
            },
            hide_index=True,
            use_container_width=True
        )
    except Exception:
        edited = plan
        st.dataframe(plan, use_container_width=True)

    # Detect changes
    if not edited.equals(plan):
        diffs = (edited != plan)
        changed_rows = diffs.any(axis=1)
        changed_idx = edited[changed_rows].index.tolist()
        for i in changed_idx:
            old = plan.loc[i]
            new = edited.loc[i]
            if (old.get("Status") == False or old.get("Status") == 0) and (new.get("Status") == True or new.get("Status") == 1):
                if new.get("Activity") == "Study 📖":
                    priority = 3
                    topic_map = st.session_state.get("topic_priority_map", {})
                    priority = topic_map.get(new.get("Details"), 3)
                    task_details = {
                        "Date": new.get("Date"),
                        "Day": new.get("Day"),
                        "Start Time": new.get("Start Time"),
                        "Details": new.get("Details"),
                        "Actual Duration (min)": int(new.get("Actual Duration (min)", 0))
                    }
                    log_completion_event(task_details, priority)
        st.session_state.study_plan_df = edited
        update_gamification(edited)
        st.rerun()

    # KPIs
    study_tasks = st.session_state.study_plan_df[st.session_state.study_plan_df['Activity'] == "Study 📖"]
    total = len(study_tasks)
    completed = int(study_tasks['Status'].sum()) if total>0 else 0
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Study Sessions", total)
    col2.metric("Completed", completed)
    col3.metric("Progress", f"{int((completed/total)*100) if total>0 else 0}%")
    col4.metric("Streak (days)", st.session_state.get("study_streak", 0))

    if completed == total and total > 0:
        st.success("🎉 Congrats! You’ve completed all planned sessions for today.")
