# 🤖 GeniusPlan AI - Adaptive Scheduler

An intelligent adaptive study planner built with **Streamlit**, designed to help students prepare more effectively by dynamically adjusting their schedules. The app leverages **machine learning (ML)** models to suggest study patterns, handle “exam tomorrow” scenarios, and continuously improve with user feedback.

---

## ✨ Features

* 📅 **Adaptive Scheduler** – Generates personalized study plans.
* ⏳ **Exam Tomorrow Mode** – Prioritizes urgent topics when exams are near.
* 🔄 **Retrain Adaptive Model** – Updates the ML model with the latest performance & study habits.
* 💾 **State Persistence** – Saves past interactions and model states so progress isn’t lost after refresh.
* 📊 **Interactive Dashboard** – View schedules, progress, and performance trends.
* 🚀 **Streamlit-powered Web App** – Simple UI with real-time updates.

---

## 🛠️ Tech Stack

* **Frontend & Backend**: Streamlit
* **ML Model**: scikit-learn, joblib
* **Data Handling**: pandas
* **Other Utilities**: Python Standard Libraries

---

## 📂 Project Structure

```
├── app.py                # Main Streamlit app
├── model/                # Saved ML models (joblib files)
├── data/                 # Training & user data
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to set up and run the app locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SaRaVaNaN0504/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Create a Virtual Environment (recommended)

```bash
python -m venv venv
```

**Activate (Windows):**

```bash
venv\Scripts\activate
```

**Activate (Mac/Linux):**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

The app will start on **[http://localhost:8501/](http://localhost:8501/)** 🚀

---

## 🌐 Deployment

### Deploy on **Streamlit Cloud**

1. Push your repo to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo.
4. Select branch → `main` and file → `app.py`.
5. Deploy 🎉

### Deploy on **Render / Hugging Face Spaces** (Optional)

* **Render**: Create a Web Service → Select repo → Add `start: streamlit run app.py` in **Procfile**.
* **Hugging Face Spaces**: Choose Streamlit template → Connect repo → Deploy.

---

## 📊 Usage

* Select **Exam Tomorrow Mode** if you need a compressed urgent schedule.
* Use **Retrain Adaptive Model** when new performance feedback is available.
* Explore your **schedule, progress, and adjustments** in the dashboard.

---

## 📜 License

This project is licensed under the **MIT License** – free to use, modify, and distribute.

---

## 👨‍💻 Author

Developed by **Saravanan**
