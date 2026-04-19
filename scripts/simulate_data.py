import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "speed": np.random.normal(40, 15, 200),  # km/h
    "acceleration": np.random.normal(0, 2, 200),
    "gyro": np.random.normal(0, 1, 200)  # turning
}

df = pd.DataFrame(data)

# Add timestamp
df["time"] = pd.date_range(start="2026-01-01", periods=200, freq="S")

df.to_csv("data/simulated_data.csv", index=False)

print("Simulated data created!")
