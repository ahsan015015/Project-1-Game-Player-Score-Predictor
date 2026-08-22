import pandas as pd                                  # CSV পড়তে
from sklearn.model_selection import train_test_split # ডেটা ভাগ করতে
from sklearn.linear_model import LinearRegression    # মডেল
import joblib                                        # মডেল সেভ করতে



data = pd.read_csv("data/game_data.csv")
print(data.head())   # প্রথম ৫টা সারি দেখাবে — চেক করার জন্য


X = data[["play_time", "enemies_killed", "damage_taken", "balls_collected"]]
y = data["score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()      # খালি মডেল
model.fit(X_train, y_train)     # fit() = ডেটা থেকে শেখা

print("R² score:", model.score(X_test, y_test))
joblib.dump(model, "models/score_model.pkl")
print("model saved successfully!")