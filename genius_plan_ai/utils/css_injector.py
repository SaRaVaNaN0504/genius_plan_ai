import streamlit as st

def inject_custom_css():
    st.markdown(
        """
        <style>
        /* 💜 Sidebar - Beautiful Pink to Violet Gradient */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ffeef8, #e8d5f2, #d4c5f9);
            box-shadow: 2px 0 10px rgba(0,0,0,0.05);
        }
        
        /* Sidebar text readable */
        section[data-testid="stSidebar"] .css-1d391kg,
        section[data-testid="stSidebar"] .css-1n76uvr {
            color: #8b4789 !important;
            font-weight: 500;
        }
        
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3 {
            color: #6a1b9a !important;
            font-family: 'Poppins', sans-serif;
            text-shadow: 0 2px 4px rgba(106, 27, 154, 0.1);
        }   

        /* 🎨 Main Dashboard Background - Dreamy Pink-Violet Gradient */
        .stApp {
            background: linear-gradient(135deg, 
                #fff0f6 0%, 
                #ffe5f1 25%, 
                #f3e5f5 50%, 
                #e1d4f7 75%, 
                #d4c5f9 100%);
            background-attachment: fixed;
        }

        /* 📌 Cards */
        .stMarkdown, .stText, .stAlert {
            background: rgba(255, 255, 255, 0.9);
            padding: 15px;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(139, 71, 137, 0.15);
            transition: transform 0.2s;
            border: 1px solid rgba(255, 182, 193, 0.3);
        }
        .stMarkdown:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 16px rgba(139, 71, 137, 0.2);
        }

        /* ✨ Buttons - Matching Pink-Violet Theme */
        div.stButton > button {
            background: linear-gradient(45deg, #d946ef, #a855f7, #ec4899);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.6em 1.2em;
            font-weight: 600;
            font-size: 0.95em;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 10px rgba(217, 70, 239, 0.3);
        }
        div.stButton > button:hover {
            background: linear-gradient(45deg, #ec4899, #f472b6, #d946ef);
            transform: scale(1.05);
            box-shadow: 0 6px 14px rgba(236, 72, 153, 0.4);
        }

        /* 🟣 Chat Input + Send Button */
        input[type="text"] {
            border-radius: 12px !important;
            border: 2px solid #d946ef !important;
            padding: 0.6em !important;
            background: rgba(255, 255, 255, 0.95) !important;
        }
        
        input[type="text"]:focus {
            border-color: #a855f7 !important;
            box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.1) !important;
        }

        /* Chat history bubbles - Pink-Violet Theme */
        .chat-bubble-user {
            background: linear-gradient(135deg, #d946ef, #a855f7);
            color: white;
            padding: 10px 14px;
            border-radius: 15px 15px 0px 15px;
            margin: 5px 0;
            display: inline-block;
            max-width: 80%;
            box-shadow: 0 3px 8px rgba(217, 70, 239, 0.3);
        }
        .chat-bubble-bot {
            background: linear-gradient(135deg, #fce7f3, #f3e8ff);
            color: #701a75;
            padding: 10px 14px;
            border-radius: 15px 15px 15px 0px;
            margin: 5px 0;
            display: inline-block;
            max-width: 80%;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(217, 70, 239, 0.2);
        }

        /* 📚 Titles */
        h1, h2, h3 {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            background: linear-gradient(90deg, #d946ef, #a855f7, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* 🎯 Additional Enhancements */
        
        /* Metrics styling */
        [data-testid="stMetricValue"] {
            color: #a855f7 !important;
            font-weight: 700;
        }
        
        /* Success/Info boxes matching theme */
        .stSuccess {
            background: linear-gradient(135deg, #fce7f3, #f3e8ff) !important;
            border-left: 4px solid #d946ef !important;
        }
        
        .stInfo {
            background: linear-gradient(135deg, #f3e8ff, #fce7f3) !important;
            border-left: 4px solid #a855f7 !important;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #d946ef, #a855f7);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, #ec4899, #d946ef);
        }
        
        /* Dataframe styling */
        [data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(139, 71, 137, 0.15);
            border: 1px solid rgba(217, 70, 239, 0.2);
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            background: rgba(255, 255, 255, 0.5);
            border-radius: 12px;
            padding: 5px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px;
            color: #a855f7;
            font-weight: 600;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(45deg, #d946ef, #a855f7);
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    