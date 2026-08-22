import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn import metrics       
import matplotlib
matplotlib.use("Agg")                 
import matplotlib.pyplot as plt



data = pd.read_csv("data/game_data.csv")
X = data[["play_time", "enemies_killed", "damage_taken", "balls_collected"]]
y = data["score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = joblib.load("models/score_model.pkl")


y_pred = model.predict(X_test)

mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
r2  = metrics.r2_score(y_test, y_pred)


print("MAE :", mae)
print("MSE :", mse)
print("R²  :", r2)


plt.scatter(y_test, y_pred, color="steelblue")   
plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Actual vs Predicted")
lims = [0, max(y_test.max(), y_pred.max())]
plt.plot(lims, lims, "r--")   # লাল ড্যাশড লাইন
plt.savefig("models/evaluation_plot.png")        
print("graph saved successfully!")