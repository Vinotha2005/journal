import streamlit as st
import pandas as pd
import os
from datetime import date

from logic.phase_splitter import split_sentences
from logic.segmentation import health_type, level_type
from logic.painway_classifier import painway_type
from logic.metrics import compute_metrics
from logic.search import search_journals
from logic.question_answer import answer_question
from logic.phase_splitter import split_sentences


DATA_PATH = "data/journals.csv"

# ---------------- DATA ----------------
def load_df():
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame(columns=["date", "journal"])
    return pd.read_csv(DATA_PATH)

def save_df(df):
    df.to_csv(DATA_PATH, index=False)

# ---------------- UI ----------------
st.set_page_config(page_title="Personal Productivity Journal", layout="wide")
st.title("📘 Personal Productivity & Reflection System")
st.caption("Turn journaling into measurable personal growth")

menu = st.sidebar.radio(
    "Menu",
    ["➕ Add Journal", "🧠 Segment Journal", "📊 Metrics", "❓ Ask Questions"]
)

# ---------------- ADD JOURNAL ----------------
if menu == "➕ Add Journal":
    st.subheader("📝 Add Daily Journal")

    d = st.date_input("Date", value=date.today())
    text = st.text_area("Write your full-day journaling", height=250)

    if st.button("Save Journal"):
        if text.strip():
            df = load_df()
            df.loc[len(df)] = [str(d), text]
            save_df(df)
            st.success("Journal saved successfully ✅")
        else:
            st.warning("Journal cannot be empty")

# ---------------- SEGMENT JOURNAL ----------------
elif menu == "🧠 Segment Journal":
    st.subheader("🧠 Structured Journal Segmentation")

    df = load_df()
    if df.empty:
        st.info("No journals available")
    else:
        idx = st.selectbox(
            "Select Date",
            df.index,
            format_func=lambda i: df.loc[i, "date"]
        )

        journal = df.loc[idx, "journal"]
        sentences = split_sentences(journal)

        structure = {
            "Macro": {"Healthy": {"Existing": [], "Possible": []},
                      "Unhealthy": {"Existing": [], "Possible": []}},
            "Micro": {"Healthy": {"Existing": [], "Possible": []},
                      "Unhealthy": {"Existing": [], "Possible": []}},
            "Nano":  {"Healthy": {"Existing": [], "Possible": []},
                      "Unhealthy": {"Existing": [], "Possible": []}},
        }

        for s in sentences:
            h = health_type(s)
            l = level_type(s)
            p = painway_type(s)

            key = "Possible" if "Possible" in p else "Existing"
            structure[l][h][key].append(s)

        for level, level_data in structure.items():
            st.markdown(f"## 🔹 {level}")
            for health, health_data in level_data.items():
                st.markdown(f"### {health}")
                for path, items in health_data.items():
                    st.markdown(f"**{path} Painways**")
                    if not items:
                        st.caption("— No entries —")
                    else:
                        for i in items:
                            st.markdown(f"- {i}")

# ---------------- METRICS ----------------
elif menu == "📊 Metrics":
    st.subheader("📊 Daily Productivity Metrics")

    df = load_df()
    if df.empty:
        st.info("No journals available")
    else:
        idx = st.selectbox(
            "Select Date",
            df.index,
            format_func=lambda i: df.loc[i, "date"]
        )

        scores = compute_metrics(df.loc[idx, "journal"])

        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("😊 Positivity", scores["positivity"])
        c2.metric("😠 Anger", scores["anger"])
        c3.metric("😓 Stress", scores["stress"])
        c4.metric("📈 Improvement", scores["improvement"])
        c5.metric("🔥 Productivity", scores["productivity"])

        st.progress(scores["productivity"] / 100)

# ---------------- ASK QUESTIONS ----------------
elif menu == "❓ Ask Questions":
    st.subheader("❓ Ask Across All Journals")

    q = st.text_input("Ask a question", placeholder="When did I use zapier?")
    if st.button("Search"):
        results = answer_question(q)

        if not results:
            st.info("No matching entries found")
        else:
            for r in results:
                st.markdown(f"### 📅 {r['date']}")
                for m in r["matches"]:
                    st.markdown(f"- {m}")
                with st.expander("Show full journal"):
                    st.write(r["full"])
