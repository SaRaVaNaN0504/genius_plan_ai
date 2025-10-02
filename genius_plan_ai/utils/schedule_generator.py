# Genius_plan_ai/utils/schedule_generator.py
import pandas as pd
from datetime import datetime, timedelta
import random
from genius_plan_ai.utils.ml_utils import load_ml_model, predict_session_duration
from genius_plan_ai.config import MOTIVATIONAL_MESSAGES

# Extra filler tasks when chapters are finished
EXTRA_TASKS = [
    "📝 Make Notes for {topic}",
    "🔁 Revise {topic}",
    "✍️ Practice Questions on {topic}",
    "⚡ Last-minute Quick Recap of {topic}"
]

def generate_ultimate_plan(
    chapter_details, 
    start_date, 
    end_date, 
    study_start_time, 
    study_end_time, 
    session_duration, 
    break_duration, 
    meal_times, 
    exam_mode=False
):
    """Generate a structured study plan with meals, breaks, and filler tasks."""

    model = load_ml_model()

    # Sort chapters by priority first (High → Medium → Low), then subject, then chapter
    chapter_details = sorted(
        chapter_details,
        key=lambda x: (x['priority'], x['subject'], x['chapter'])
    )

    topics = [
        {
            "name": f"{c['subject']} - {c['chapter']}",
            "priority": c['priority'],
            "subject": c['subject']
        }
        for c in chapter_details
    ]

    plan = []
    topic_index = 0
    current_date = start_date

    while current_date <= end_date:
        day_start = datetime.combine(current_date, study_start_time)
        day_end = datetime.combine(current_date, study_end_time)

        # --------------------------
        # Insert Meal Times
        # --------------------------
        meal_blocks = []
        for meal_name, meal in meal_times.items():
            meal_start = datetime.combine(current_date, meal['start'])
            meal_end = meal_start + timedelta(minutes=meal['duration'])
            if meal_end > day_start and meal_start < day_end:
                plan.append({
                    "Date": current_date.strftime("%Y-%m-%d"),
                    "Day": current_date.strftime("%A"),
                    "Start Time": meal_start.strftime("%H:%M"),
                    "End Time": meal_end.strftime("%H:%M"),
                    "Activity": "Meal Break 🍽️",
                    "Details": meal_name.capitalize(),
                    "Actual Duration (min)": meal['duration']
                })
                meal_blocks.append((meal_start, meal_end))
        meal_blocks.sort()

        # --------------------------
        # Available slots between meals
        # --------------------------
        available_slots = []
        last_end = day_start
        for s, e in meal_blocks:
            if last_end < s:
                available_slots.append((last_end, s))
            last_end = max(last_end, e)
        if last_end < day_end:
            available_slots.append((last_end, day_end))

        # --------------------------
        # Fill Study Sessions & Breaks
        # --------------------------
        for slot_start, slot_end in available_slots:
            current_time = slot_start
            while current_time < slot_end:
                if topic_index < len(topics):
                    # Pick next chapter
                    cur_topic = topics[topic_index]
                    eff_dur = predict_session_duration(
                        model,
                        cur_topic['subject'],
                        cur_topic['priority'],
                        session_duration
                    )

                    # Slightly shorter evening sessions
                    if current_time.hour >= 18:
                        eff_dur = max(15, int(eff_dur * 0.9))

                    session_end = current_time + timedelta(minutes=eff_dur)
                    if session_end > slot_end:
                        break

                    # Add study session
                    plan.append({
                        "Date": current_date.strftime("%Y-%m-%d"),
                        "Day": current_date.strftime("%A"),
                        "Start Time": current_time.strftime("%H:%M"),
                        "End Time": session_end.strftime("%H:%M"),
                        "Activity": "Study 📖",
                        "Details": cur_topic['name'],
                        "Actual Duration (min)": eff_dur
                    })

                    topic_index += 1
                    current_time = session_end
                else:
                    # --------------------------
                    # No chapters left → filler activity
                    # --------------------------
                    filler_topic = random.choice(topics)['name'] if topics else "General Revision"
                    filler_task = random.choice(EXTRA_TASKS).format(topic=filler_topic)

                    session_end = current_time + timedelta(minutes=session_duration)
                    if session_end > slot_end:
                        break

                    plan.append({
                        "Date": current_date.strftime("%Y-%m-%d"),
                        "Day": current_date.strftime("%A"),
                        "Start Time": current_time.strftime("%H:%M"),
                        "End Time": session_end.strftime("%H:%M"),
                        "Activity": "Study 📖",
                        "Details": filler_task,
                        "Actual Duration (min)": session_duration
                    })
                    current_time = session_end

                # --------------------------
                # Insert break after session
                # --------------------------
                break_end = current_time + timedelta(minutes=break_duration)
                if break_end <= slot_end:
                    plan.append({
                        "Date": current_date.strftime("%Y-%m-%d"),
                        "Day": current_date.strftime("%A"),
                        "Start Time": current_time.strftime("%H:%M"),
                        "End Time": break_end.strftime("%H:%M"),
                        "Activity": "Break ☕️",
                        "Details": random.choice(
                            MOTIVATIONAL_MESSAGES + ["💧 Stay Hydrated", "🌿 Stretch for 5 min"]
                        ),
                        "Actual Duration (min)": break_duration
                    })
                    current_time = break_end
                else:
                    break

        current_date += timedelta(days=1)
        if exam_mode:
            break  # Only one day if exam tomorrow

    # --------------------------
    # Return structured DataFrame
    # --------------------------
    if not plan:
        return pd.DataFrame()

    df = pd.DataFrame(plan)

    # Ensure chronological order
    df["start_dt"] = pd.to_datetime(
        df["Date"].astype(str) + " " + df["Start Time"], 
        format="%Y-%m-%d %H:%M"
    )
    df = df.sort_values(by=["Date", "start_dt"]).drop(columns=["start_dt"]).reset_index(drop=True)

    # Add status column if missing
    if "Status" not in df.columns:
        df.insert(0, "Status", False)

    return df
