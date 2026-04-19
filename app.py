import streamlit as st
from scripts.scoring import calculate_score

st.title("🏍️ Driving Behavior Score")

score = calculate_score()

st.metric("Driving Score", score)

if score > 80:
    st.success("Safe Driving 👍")
elif score > 50:
    st.warning("Moderate Driving ⚠️")
else:
    st.error("Risky Driving 🚨")
