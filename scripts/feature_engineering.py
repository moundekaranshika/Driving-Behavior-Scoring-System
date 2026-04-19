import pandas as pd

def process_data():
    df = pd.read_csv("data/simulated_data.csv")

    # Rolling averages (realistic behavior)
    df["speed_avg"] = df["speed"].rolling(window=5).mean()
    df["acc_avg"] = df["acceleration"].rolling(window=5).mean()

    # Behavior detection
    df["speeding"] = df["speed"] > 60
    df["harsh_braking"] = df["acceleration"] < -4
    df["rapid_acceleration"] = df["acceleration"] > 4
    df["sharp_turn"] = df["gyro"].abs() > 2

    df.fillna(0, inplace=True)

    df.to_csv("data/processed_data.csv", index=False)

if __name__ == "__main__":
    process_data()
