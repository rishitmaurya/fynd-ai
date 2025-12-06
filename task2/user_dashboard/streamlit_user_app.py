# streamlit_user_app.py
import streamlit as st
import requests
import os

st.set_page_config(page_title="User Feedback", layout="centered")
st.title("User Feedback Portal")

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
SUBMIT_ENDPOINT = f"{BACKEND_URL}/submit"

with st.form("feedback_form"):
    rating = st.selectbox("Select a star rating", [5,4,3,2,1], index=0)
    review = st.text_area("Write a short review", height=160)
    submitted = st.form_submit_button("Submit")

if submitted:
    if not review.strip():
        st.warning("Please enter a short review.")
    else:
        payload = {"rating": rating, "review": review}
        try:
            res = requests.post(SUBMIT_ENDPOINT, json=payload, timeout=30)
            if res.status_code == 200:
                data = res.json()
                st.success("Thank you — AI reply below:")
                st.markdown("**AI reply to user**")
                st.write(data.get("ai_reply"))
                st.markdown("**Saved record**")
                st.json(data)
            else:
                st.error(f"Server error: {res.status_code} — {res.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")
