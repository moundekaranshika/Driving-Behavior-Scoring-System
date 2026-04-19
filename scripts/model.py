import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    df = pd.read_csv("data/processed_data.csv")

    # Label: risky driving
    df["label"] = (
        df["speeding"] |
        df["harsh_braking"] |
        df["rapid_acceleration"] |
        df["sharp_turn"]
    )

    X = df[["speed", "acceleration", "gyro"]]
    y = df["label"]

    model = RandomForestClassifier()
    model.fit(X, y)

    print("Model trained successfully!")

if __name__ == "__main__":
    train_model()
