import pandas as pd
import joblib

model = joblib.load("models/score_model.pkl")

player = pd.DataFrame([{
    "play_time": 60,
    "enemies_killed": 12,
    "damage_taken": 25,
    "balls_collected": 8
}])

result = model.predict(player)
print("Predicted Score:", result[0])