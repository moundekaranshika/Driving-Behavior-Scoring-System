import pandas as pd

def calculate_score():
    df = pd.read_csv("data/processed_data.csv")

    penalties = (
        df["speeding"].sum() * 2 +
        df["harsh_braking"].sum() * 3 +
        df["rapid_acceleration"].sum() * 2 +
        df["sharp_turn"].sum() * 2
    )

    score = max(0, 100 - penalties)

    print(f"Driving Score: {score}")

    return score

if __name__ == "__main__":
    calculate_score()
