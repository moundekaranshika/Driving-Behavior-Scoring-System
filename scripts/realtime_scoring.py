def detect_events(data):
    return {
        "speeding": data["speed"] > 60,
        "harsh_braking": data["acceleration"] < -4,
        "rapid_acceleration": data["acceleration"] > 4,
        "sharp_turn": abs(data["gyro"]) > 2
    }

def update_score(score, events):
    penalty = (
        events["speeding"] * 2 +
        events["harsh_braking"] * 3 +
        events["rapid_acceleration"] * 2 +
        events["sharp_turn"] * 2
    )
    return max(0, score - penalty)
