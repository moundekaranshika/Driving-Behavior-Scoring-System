import streamlit as st
import pandas as pd
from scripts.scoring import calculate_score

st.title("🏍️ Driving Behavior Analytics")

df = pd.read_csv("data/processed_data.csv")

score = calculate_score()

st.metric("Driving Score", f"{score:.2f}")

st.line_chart(df["speed"], height=200)
st.line_chart(df["acceleration"], height=200)

st.subheader("Event Counts")
st.write({
    "Speeding": int(df["speeding"].sum()),
    "Harsh Braking": int(df["harsh_braking"].sum()),
    "Sharp Turns": int(df["sharp_turn"].sum())
})
