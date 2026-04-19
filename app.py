import streamlit as st
import time
import pandas as pd
from collections import deque

from scripts.stream_data import data_stream
from scripts.realtime_scoring import detect_events, update_score
from scripts.model import train_model, predict_risk

st.set_page_config(layout="wide")
st.title("🏍️ AI-Powered Rider Safety System")

# Train ML model
model = train_model()

# Buffers
max_points = 50
speed_data = deque(maxlen=max_points)
acc_data = deque(maxlen=max_points)
score_data = deque(maxlen=max_points)

lat_data = deque(maxlen=max_points)
lon_data = deque(maxlen=max_points)

score = 100
stream = data_stream()

col1, col2 = st.columns(2)
chart_speed = col1.empty()
chart_acc = col2.empty()
map_placeholder = st.empty()
metrics = st.empty()

for data in stream:
    # Extract values
    speed = data["speed"]
    acc = data["acceleration"]
    gyro = data["gyro"]
    lat = data["lat"]
    lon = data["lon"]

    # Detect events
    events = detect_events(data)

    # Update score
    score = update_score(score, events)

    # ML prediction
    risk = predict_risk(model, data)

    # Store data
    speed_data.append(speed)
    acc_data.append(acc)
    score_data.append(score)
    lat_data.append(lat)
    lon_data.append(lon)

    df = pd.DataFrame({
        "Speed": list(speed_data),
        "Acceleration": list(acc_data),
        "Score": list(score_data)
    })

    # Charts
    chart_speed.line_chart(df["Speed"])
    chart_acc.line_chart(df["Acceleration"])

    # Map
    map_df = pd.DataFrame({
        "lat": list(lat_data),
        "lon": list(lon_data)
    })
    map_placeholder.map(map_df)

    # Metrics + Alerts
    with metrics.container():
        st.metric("🚗 Speed", f"{speed:.2f} km/h")
        st.metric("🎯 Driving Score", f"{score}")

        if events["speeding"]:
            st.error("🚨 Speeding detected!")
        if events["harsh_braking"]:
            st.warning("⚠️ Harsh braking!")
        if events["sharp_turn"]:
            st.warning("⚠️ Sharp turn!")

        if risk == 1:
            st.error("🚨 High Risk Driving Predicted!")

    # Score graph
    st.line_chart(df["Score"])

    # Report download
    st.download_button(
        "📥 Download Driving Report",
        df.to_csv().encode(),
        "driving_report.csv"
    )

    time.sleep(1)
