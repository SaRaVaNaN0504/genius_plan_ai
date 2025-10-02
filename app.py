# app.py (root)
import streamlit as st
from genius_plan_ai.components.sidebar import render_sidebar
from genius_plan_ai.components.main_dashboard import render_main_dashboard
from genius_plan_ai.components.ai_companion import render_ai_companion
from genius_plan_ai.components.export_retrain import render_export_retrain
from genius_plan_ai.utils.css_injector import inject_custom_css
from genius_plan_ai.utils.gamification_manager import initialize_gamification


st.set_page_config(
    page_title="GeniusPlan AI",
    page_icon="✨",
    layout="wide"
)


# Page setup
st.set_page_config(page_title="GeniusPlan AI - Adaptive Scheduler", layout="wide")
inject_custom_css()
initialize_gamification()

# Layout
with st.sidebar:
    render_sidebar()

col_main, col_right = st.columns([3,1])
with col_main:
    st.markdown("<h1 style='text-align:center'>✨ GeniusPlan AI ✨</h1>", unsafe_allow_html=True)
    render_main_dashboard()
    st.markdown("---")
    render_ai_companion()  # upgraded with motivation + greetings

with col_right:
    render_export_retrain()
