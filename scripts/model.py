import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_model():
    df = pd.read_csv("data/processed_data.csv")

    df["label"] = (
        df["speeding"] |
        df["harsh_braking"] |
        df["rapid_acceleration"] |
        df["sharp_turn"]
    )

    X = df[["speed", "acceleration", "gyro", "speed_avg", "acc_avg"]]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print(classification_report(y_test, preds))

if __name__ == "__main__":
    train_model()
