import streamlit as st
import random

# --- Predefined responses ---
MOTIVATIONAL_QUOTES = [
    "💡 Every session brings you closer to your goals.",
    "🌱 The expert in anything was once a beginner. Keep learning!",
    "🔥 Small progress each day adds up to big results.",
    "🚀 Success is the sum of consistent efforts, repeated daily.",
    "📖 One chapter at a time, you're mastering your future.",
    "💪 You're capable of amazing things. Keep pushing forward!",
    "⭐ Believe in yourself and all that you are.",
    "🎯 Your only limit is the one you set for yourself."
]

GREETING_RESPONSES = [
    "👋 Hey there! Ready to crush your study goals?",
    "✨ Hi! Let's make today productive.",
    "🌞 Hello! Time to focus and shine.",
    "🤖 Hey! Your AI companion is here for you.",
    "💜 Welcome back! Let's achieve greatness together.",
    "🎓 Greetings, scholar! Ready for an amazing study session?"
]

STUDY_TIPS = [
    "📌 Use Pomodoro: 25 mins study, 5 mins break.",
    "📝 Make handwritten notes to retain better.",
    "🎯 Revise after every 2 chapters.",
    "🥤 Stay hydrated while studying.",
    "🧠 Teach concepts to others to solidify understanding.",
    "🎵 Try white noise or lo-fi music for better focus.",
    "📱 Keep your phone away during study sessions.",
    "😴 Get 7-8 hours of sleep for optimal memory retention."
]

STRESS_RELIEF = [
    "😌 Take 5 deep breaths: inhale for 4, hold for 4, exhale for 4.",
    "🚶‍♀️ Take a short walk outside to clear your mind.",
    "🎨 Try a creative break: doodle, color, or journal.",
    "🧘 Do a quick 5-minute meditation or stretching.",
    "💆 Remember: Breaks are productive. Your brain needs rest!"
]

ENCOURAGEMENT = [
    "You're doing amazing! Keep going! 💪",
    "I believe in you! You've got this! ⭐",
    "Progress, not perfection. You're on the right track! 🌟",
    "Every step forward is a victory! Celebrate it! 🎉"
]




def get_chatbot_response(user_input: str) -> str:
    """Return intelligent chatbot response based on input with improved pattern matching."""
    text = user_input.lower().strip()
    
    # Greetings
    if any(word in text for word in ["hi", "hello", "hey", "hola", "greetings"]):
        return random.choice(GREETING_RESPONSES)
    
    # Motivation requests
    elif any(word in text for word in ["motivate", "motivation", "inspire", "encourage"]):
        return random.choice(MOTIVATIONAL_QUOTES)
    
    # Study tips
    elif any(phrase in text for phrase in ["tip", "study", "how to", "help me learn", "focus"]):
        return random.choice(STUDY_TIPS)
    
    # Stress/anxiety
    elif any(word in text for word in ["stress", "anxious", "worried", "nervous", "overwhelmed"]):
        return random.choice(STRESS_RELIEF)
    
    # Exam preparation
    elif "exam" in text and any(word in text for word in ["tomorrow", "soon", "coming", "next week"]):
        return "📅 Don't panic! Focus on high-weightage topics first. Quick revision > Deep dive now. You've got this! 💪"
    
    # Gratitude
    elif any(word in text for word in ["thank", "thanks", "appreciate"]):
        return "You're very welcome! Happy to help you succeed! 🌟"
    
    # Goodbyes
    elif any(word in text for word in ["bye", "goodbye", "see you", "later"]):
        return "See you soon! Keep up the great work! 👋✨"
    
    # Asking about the bot
    elif any(phrase in text for phrase in ["who are you", "what are you", "your name"]):
        return "🤖 I'm your AI Study Companion! I'm here to motivate, guide, and support your learning journey! 💜"
    
    # Positive feedback
    elif any(word in text for word in ["good", "great", "awesome", "amazing"]):
        return random.choice(ENCOURAGEMENT)
    
    # Confusion/difficulty
    elif any(word in text for word in ["confused", "difficult", "hard", "struggling", "don't understand"]):
        return "🤔 Break it down into smaller parts. Start with the basics, then build up. You can do this step by step! 📚"
    
    # Time management
    elif any(word in text for word in ["time", "schedule", "plan", "organize"]):
        return "⏰ Try time-blocking: Assign specific hours to subjects. Prioritize tough topics when you're most alert! 🎯"
    
    # Default response with suggestions
    else:
        suggestions = [
            "💬 Try asking me:",
            "   • 'Motivate me'",
            "   • 'Give me a study tip'",
            "   • 'I'm feeling stressed'",
            "   • 'Exam tomorrow, help!'"
        ]
        return "\n".join(suggestions)
    
    
def render_ai_companion():
    st.title("🤖 AI Companion")
    st.caption("Ask the companion anything — motivation, greetings, or study tips!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # --- Chat Input with SEND button inline ---
    with st.container():
        col1, col2 = st.columns([6, 1])
        with col1:
            user_input = st.text_input(
                "Ask the companion...",
                key="chat_input",
                label_visibility="collapsed",
                placeholder="Type your message..."
            )
        with col2:
            send = st.button("Send", use_container_width=True)

    if send and user_input.strip():
        # Store user message
        st.session_state.chat_history.append(("You", user_input))

        # Get response
        bot_reply = get_chatbot_response(user_input)
        st.session_state.chat_history.append(("Companion", bot_reply))

        # Clear input safely
        st.session_state.pop("chat_input", None)
        st.rerun()  # rerun to refresh input field

    # --- Display chat history ---
    for role, message in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Companion:** {message}")
