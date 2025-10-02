# genius_plan_ai/config.py

import os
from datetime import time

# --- Paths ---
MODELS_DIR = "models"
DATA_DIR = "data"
LOG_FILE = os.path.join(DATA_DIR, 'study_log.csv')
ML_MODEL_PATH = os.path.join(MODELS_DIR, 'duration_predictor_model.pkl')

# Ensure data and models directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)


# --- Default Session Settings ---
DEFAULT_STUDY_START_TIME = time(9, 0)
DEFAULT_STUDY_END_TIME = time(21, 0)
DEFAULT_SESSION_DURATION = 45 # minutes
DEFAULT_BREAK_DURATION = 15   # minutes

# --- Meal Times ---
DEFAULT_MEAL_TIMES = {
    "breakfast": {"start": time(8, 0), "duration": 30},
    "lunch": {"start": time(13, 0), "duration": 60},
    "dinner": {"start": time(19, 0), "duration": 45}
}

# --- Gamification ---
ACHIEVEMENTS_MAP = {
    "First Streak": lambda state: state.get('study_streak', 0) >= 3,
    "Week Warrior": lambda state: state.get('study_streak', 0) >= 7,
    "Month Master": lambda state: state.get('study_streak', 0) >= 30,
    "Getting Started": lambda state: state.get('total_sessions_completed', 0) >= 10,
    "Dedicated Learner": lambda state: state.get('total_sessions_completed', 0) >= 50,
    "Study Legend": lambda state: state.get('total_sessions_completed', 0) >= 100,
}

# --- AI Companion ---
INTENT_MAP = {
    'get_schedule': ['schedule', 'plan', 'agenda', 'calendar', 'timetable'],
    'get_next_task': ['next', 'what is next', 'next task', 'upcoming'],
    'query_high_priority': ['high priority', 'important tasks', 'critical', 'urgent'],
    'handle_missed_session': ['missed', 'skipped', 'fell behind', 'catch up'],
    'request_motivation': ['motivation', 'motivate me', 'encourage', 'pep talk'],
    'get_progress': ['progress', 'how am i doing', 'overall status']
}

# --- Motivational Messages ---
MOTIVATIONAL_MESSAGES = [
    "🚀 You're doing amazing! Keep pushing forward.",
    "💡 Every session brings you closer to your goals.",
    "🧠 Your brain is a muscle; keep training it!",
    "🌟 Believe in yourself and all that you are. You have this!",
    "🎯 Stay focused, stay determined, stay unstoppable.",
    "💪 Success is the sum of small efforts, repeated day in and day out.",
    "🌱 The expert in anything was once a beginner. Keep learning!",
    "🐢 Slow and steady wins the race. Consistency is key.",
    "🏆 Envision your success and work backward. You got this!",
    "✨ Make today count! Each step is progress."
]