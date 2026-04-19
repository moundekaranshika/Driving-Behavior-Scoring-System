import time
import numpy as np
from datetime import datetime

def data_stream():
    speed = 30
    lat, lon = 19.07, 72.87  # starting location

    while True:
        speed += np.random.normal(0, 2)

        acceleration = np.random.normal(0, 2)
        gyro = np.random.normal(0, 0.5)

        # Add occasional risky events
        if np.random.rand() < 0.1:
            acceleration += np.random.choice([5, -5])

        if np.random.rand() < 0.1:
            gyro += np.random.choice([3, -3])

        # Simulate movement
        lat += np.random.normal(0, 0.0001)
        lon += np.random.normal(0, 0.0001)

        yield {
            "time": datetime.now(),
            "speed": max(0, speed),
            "acceleration": acceleration,
            "gyro": gyro,
            "lat": lat,
            "lon": lon
        }

        time.sleep(1)
