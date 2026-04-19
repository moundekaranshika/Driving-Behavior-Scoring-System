import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

np.random.seed(42)

n = 300
time = pd.date_range(start="2026-01-01", periods=n, freq="s")

# Simulate smooth driving
speed = []
current_speed = 20

for _ in range(n):
    change = np.random.normal(0, 2)
    current_speed = max(0, current_speed + change)
    speed.append(current_speed)

speed = np.array(speed)

# Acceleration (derivative of speed)
acceleration = np.diff(speed, prepend=speed[0])

# Add occasional harsh events
for i in range(0, n, 50):
    acceleration[i] += np.random.choice([5, -5])

# Gyroscope (turning)
gyro = np.random.normal(0, 0.5, n)

# Add sharp turns occasionally
for i in range(25, n, 60):
    gyro[i] += np.random.choice([3, -3])

df = pd.DataFrame({
    "time": time,
    "speed": speed,
    "acceleration": acceleration,
    "gyro": gyro
})

df.to_csv("data/simulated_data.csv", index=False)

print("Realistic driving data generated!")
