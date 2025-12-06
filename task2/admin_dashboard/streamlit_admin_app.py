# streamlit_admin_app.py
import streamlit as st
import pandas as pd
import os
import requests
import time

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("Admin — Feedback Submissions")

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
SUBS_ENDPOINT = f"{BACKEND_URL}/submissions"

st.sidebar.header("Settings")
auto_refresh = st.sidebar.checkbox("Auto-refresh (10s)", value=False)
limit = st.sidebar.slider("Max rows to fetch", 10, 500, 200)

def fetch_submissions(limit):
    try:
        resp = requests.get(SUBS_ENDPOINT, params={"limit": limit}, timeout=10)
        if resp.status_code == 200:
            return pd.DataFrame(resp.json())
        else:
            st.error(f"Error fetching: {resp.status_code}")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Failed to fetch: {e}")
        return pd.DataFrame()

df = fetch_submissions(limit)

if df.empty:
    st.info("No submissions yet.")
else:
    st.sidebar.download_button("Download CSV", df.to_csv(index=False), "submissions.csv", "text/csv")
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("Recent submissions")
        st.dataframe(df[["id","timestamp","rating","review","ai_summary","ai_actions"]])
    with col2:
        st.subheader("Analytics")
        st.write("Ratings distribution")
        st.bar_chart(df['rating'].value_counts().sort_index())

    st.subheader("View submission details")
    sel_id = st.number_input("Submission ID", min_value=int(df['id'].min()), max_value=int(df['id'].max()), value=int(df['id'].max()))
    row = df[df['id'] == sel_id]
    if not row.empty:
        r = row.iloc[0]
        st.markdown(f"**Review (rating {r['rating']})**")
        st.write(r['review'])
        st.markdown("**AI Summary**")
        st.write(r['ai_summary'])
        st.markdown("**AI Suggested Actions**")
        st.write(r['ai_actions'])

if auto_refresh:
    time.sleep(10)
    st.rerun()
