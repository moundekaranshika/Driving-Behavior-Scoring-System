import pandas as pd

def calculate_score():
    df = pd.read_csv("data/processed_data.csv")

    total = len(df)

    penalties = (
        (df["speeding"].sum() / total) * 30 +
        (df["harsh_braking"].sum() / total) * 30 +
        (df["rapid_acceleration"].sum() / total) * 20 +
        (df["sharp_turn"].sum() / total) * 20
    )

    score = max(0, 100 - penalties)

    print(f"Driving Score: {score:.2f}")

    return score

if __name__ == "__main__":
    calculate_score()
