
# 📘 Personal Productivity & Reflection System

Turn daily journaling into measurable personal growth

This project is a structured journaling and productivity analysis app built with Streamlit.
It allows users to write daily journals, store them by date, segment thoughts meaningfully, and analyze emotional & productivity patterns over time.
## App : https://journal-uxy4amofztpg39oumsz8mz.streamlit.app/
## 🚀 Key Features
### 📝 Daily Journaling

Add journal entries with a specific date

Automatically stored and retrievable

Supports long, free-form journaling text

### 🧠 Intelligent Journal Segmentation

Each journal entry is automatically segmented into:

Macro / Micro / Nano levels

Healthy / Unhealthy patterns

Painways

Existing Healthy

Possible Healthy

Existing Unhealthy

Possible Unhealthy

This helps identify behavior patterns and thought loops.

### 📊 Productivity Dashboard

Visual insights for each day:

Positivity vs Improvement

Calm vs Anger

Healthy vs Unhealthy trends

Daily growth indicators

Designed to increase self-awareness and productivity.

### ❓ Ask Questions Across Journals

Ask natural questions like:

“When did I feel stressed?”

“When did I use Zapier?”

“Which days was I productive?”

The app returns:

### 📅 Date

📌 Exact matching sentences

📖 Full journal (expandable)

✏️ Edit & Delete Journals

Edit entries if a mistake was made

Delete entries with wrong dates

Safe handling of stored data

### 🗂️ Project Structure
personal_productivity_journaling/
│
├── app.py                      # Main Streamlit app
├── requirements.txt
├── README.md
│
├── logic/
│   ├── __init__.py
│   ├── phase_splitter.py       # Sentence splitting
│   ├── segmentation.py         # Health & level classification
│   ├── painway_classifier.py   # Painway logic
│   └── question_answer.py      # Ask Questions feature
│
├── data/
│   └── journals.csv            # Stored journal data

### 🛠️ Technologies Used

Python

Streamlit

Pandas

Regex (text processing)

▶️ How to Run Locally

1️⃣ Clone the repository

git clone <your-repo-link>
cd personal_productivity_journaling


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run the app

streamlit run app.py

☁️ Deployment (Streamlit Cloud)

✔ Ensure:

logic/__init__.py exists

No double-nested folders

Correct imports

Then deploy directly from GitHub using Streamlit Cloud.

### 🎯 Use Case

This app is ideal for:

Students tracking self-growth

Professionals improving productivity

Anyone practicing reflective journaling

Personal development & habit analysis

Competitions and academic projects

### 🌱 Future Enhancements

AI-based sentiment scoring

Weekly/monthly summaries

Goal tracking

Export to PDF

Authentication & user profiles

👤 Author

Vinotha S
Personal Productivity & AI-assisted Reflection Project
