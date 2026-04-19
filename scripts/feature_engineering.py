import pandas as pd

def process_data():
    df = pd.read_csv("data/simulated_data.csv")

    df["speeding"] = df["speed"] > 60
    df["harsh_braking"] = df["acceleration"] < -3
    df["rapid_acceleration"] = df["acceleration"] > 3
    df["sharp_turn"] = df["gyro"].abs() > 2

    df.to_csv("data/processed_data.csv", index=False)

if __name__ == "__main__":
    process_data()
