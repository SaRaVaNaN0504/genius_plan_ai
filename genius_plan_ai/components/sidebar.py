# Genius_plan_ai/components/sidebar.py
import streamlit as st
from datetime import datetime, date, time, timedelta
from genius_plan_ai.utils.css_injector import inject_custom_css
from genius_plan_ai.utils.schedule_generator import generate_ultimate_plan
from genius_plan_ai.config import DEFAULT_STUDY_START_TIME, DEFAULT_STUDY_END_TIME, DEFAULT_SESSION_DURATION, DEFAULT_BREAK_DURATION

def render_sidebar():
    inject_custom_css()
    st.sidebar.markdown("<h2 style='text-align:center'>🌟 GeniusPlan AI</h2>", unsafe_allow_html=True)

    if 'study_streak' not in st.session_state:
        st.session_state.study_streak = 0
        st.session_state.total_sessions_completed = 0
        st.session_state.achievements = []

    # Study parameters
    with st.sidebar.expander("🗓️ Study Parameters", expanded=True):
        col1, col2 = st.columns(2)
        study_start_time = col1.time_input("🌅 Daily Start", value=DEFAULT_STUDY_START_TIME)
        study_end_time = col2.time_input("🌙 Daily End", value=DEFAULT_STUDY_END_TIME)
        session_duration = st.slider("📚 Default Session (min)", 15, 120, DEFAULT_SESSION_DURATION, 5)
        break_duration = st.slider("☕️ Break (min)", 5, 30, DEFAULT_BREAK_DURATION, 5)

    # Meals
    meal_times = {
        "breakfast": {"start": time(8,0), "duration": 30},
        "lunch": {"start": time(13,0), "duration": 60},
        "dinner": {"start": time(19,0), "duration": 45}
    }
    with st.sidebar.expander("🍽️ Meal Breaks"):
        meal_times['breakfast']['start'] = st.time_input("🥐 Breakfast", value=meal_times['breakfast']['start'])
        meal_times['lunch']['start'] = st.time_input("🥗 Lunch", value=meal_times['lunch']['start'])
        meal_times['dinner']['start'] = st.time_input("🍝 Dinner", value=meal_times['dinner']['start'])

    # Subjects
    st.sidebar.header("📚 Subjects & Chapters")
    if "subjects" not in st.session_state:
        st.session_state.subjects = []

    with st.sidebar.form("add_subject_form", clear_on_submit=True):
        sname = st.text_input("Subject name", placeholder="Add subject and press Add")
        add_btn = st.form_submit_button("➕ Add subject")
        if add_btn and sname.strip():
            st.session_state.subjects.append({"name": sname.strip(), "chapters": []})

    for i, subj in enumerate(st.session_state.subjects):
        with st.sidebar.expander(f"📘 {subj['name']}"):
            num = st.number_input(f"Number of chapters for {subj['name']}", min_value=1, max_value=200, value=max(1,len(subj.get('chapters',[]))), key=f"num_{i}")
            chapters = subj.get('chapters', [])
            if len(chapters) < num:
                for j in range(len(chapters), num):
                    chapters.append({"chapter": f"Chapter {j+1}", "priority": 2})
            elif len(chapters) > num:
                chapters = chapters[:num]
            for j in range(num):
                p = st.selectbox(f"{subj['name']} — Chapter {j+1} priority", ["🔥 High", "🟡 Medium", "🧊 Low"], 
                                 index=0 if chapters[j]['priority']==1 else (1 if chapters[j]['priority']==2 else 2), key=f"prio_{i}_{j}")
                mapping = {"🔥 High":1, "🟡 Medium":2, "🧊 Low":3}
                chapters[j]['priority'] = mapping[p]
                chapters[j]['chapter'] = f"Chapter {j+1}"
            st.session_state.subjects[i]['chapters'] = chapters

    st.sidebar.markdown("---")
    st.sidebar.header("📅 Timeline")
    today = date.today()
    start_date = st.sidebar.date_input("Start Date", value=today, min_value=today)
    end_date = st.sidebar.date_input("End Date", value=today + timedelta(days=14), min_value=start_date)

    # 🚀 Exam Tomorrow Mode: compress into one day
    exam_tomorrow = st.sidebar.checkbox("⚡ Exam Tomorrow Mode")
    if exam_tomorrow:
        start_date = today
        end_date = today

    if st.sidebar.button("🚀 Generate My Ultimate Plan!"):
        chapter_details = []
        for subj in st.session_state.subjects:
            for chap in subj['chapters']:
                chapter_details.append({
                    "subject": subj['name'],
                    "chapter": chap['chapter'],
                    "priority": chap['priority']
                })
        if not chapter_details:
            st.sidebar.error("Add at least one subject with chapters.")
        else:
            with st.spinner("Generating plan..."):
                plan_df = generate_ultimate_plan(
                    chapter_details, start_date, end_date, 
                    study_start_time, study_end_time, session_duration, break_duration, meal_times,
                    exam_mode=exam_tomorrow
                )
                if not plan_df.empty:
                    st.session_state.study_plan_df = plan_df
                    st.sidebar.success("Plan generated — check the dashboard!")
                else:
                    st.sidebar.error("No plan could be generated. Check dates/inputs.")
    st.sidebar.markdown("---")
