import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # Dummy training data
    df = pd.DataFrame({
        "speed": [30, 80, 50, 90],
        "acceleration": [0, -5, 1, 6],
        "gyro": [0.2, 2.5, 0.5, 3],
        "label": [0, 1, 0, 1]
    })

    X = df[["speed", "acceleration", "gyro"]]
    y = df["label"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model

def predict_risk(model, data):
    X = [[data["speed"], data["acceleration"], data["gyro"]]]
    return model.predict(X)[0]
