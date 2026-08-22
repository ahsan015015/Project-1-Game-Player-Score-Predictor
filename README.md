# Project-1-Game-Player-Score-Predictor

# Game Player Score Predictor

A beginner-friendly Machine Learning project that predicts a player's game score based on gameplay statistics.

This project is designed as a first AI/ML project for developers who already have programming experience and want to learn how Machine Learning works in practice.

## 🎯 Project Goal

The goal is to train a Machine Learning model that can predict a player's score using gameplay data.

### Example

**Input:**

* Play Time: 60 seconds
* Enemies Killed: 12
* Damage Taken: 25
* Balls Collected: 8

**Output:**

```text
Predicted Score: 740
```

The model learns the relationship between player statistics and their final score from previously collected gameplay data.

## 🧠 What You'll Learn

By completing this project, you will learn the basic Machine Learning workflow:

```text
Collect Data
     ↓
Prepare Dataset
     ↓
Split Data
     ↓
Train Model
     ↓
Evaluate Model
     ↓
Make Predictions
```

You will also learn:

* Python basics for Machine Learning
* Working with datasets
* Features and labels
* Training and testing data
* Regression
* Model evaluation
* Making predictions
* Saving and loading a trained model

## 📊 Dataset

The initial dataset will contain gameplay statistics such as:

| Feature           | Description                  |
| ----------------- | ---------------------------- |
| `play_time`       | Total time the player played |
| `enemies_killed`  | Number of enemies defeated   |
| `damage_taken`    | Total damage received        |
| `balls_collected` | Number of balls collected    |
| `score`           | Final player score           |

Example:

```csv
play_time,enemies_killed,damage_taken,balls_collected,score
30,5,40,3,320
45,8,30,5,510
60,12,25,8,740
90,18,20,12,1050
```

## 🛠️ Technologies

* Python
* NumPy
* Pandas
* Scikit-learn
* Matplotlib

## 📁 Project Structure

```text
game-player-score-predictor/
│
├── data/
│   └── game_data.csv
│
├── src/
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
│
├── models/
│   └── score_model.pkl
│
├── notebooks/
│   └── exploration.ipynb
│
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd game-player-score-predictor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Machine Learning Model

The first version will use a simple **Linear Regression** model.

The model will learn:

```text
Gameplay Statistics
        ↓
Linear Regression
        ↓
Predicted Score
```

The purpose of using Linear Regression first is to understand the Machine Learning workflow before moving to more complex models.

## 📈 Training

The training process will:

1. Load the dataset.
2. Separate features and labels.
3. Split the data into training and testing sets.
4. Train the regression model.
5. Evaluate its performance.
6. Save the trained model.

Example:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = data[
    [
        "play_time",
        "enemies_killed",
        "damage_taken",
        "balls_collected"
    ]
]

y = data["score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
```

## 🔮 Making a Prediction

After training, the model can predict a score for a new player.

Example:

```python
player = [[60, 12, 25, 8]]

prediction = model.predict(player)

print("Predicted Score:", prediction[0])
```

## 📏 Model Evaluation

The model will be evaluated using metrics such as:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

The goal is not just to get a prediction, but to understand **how accurate the model is**.

## 🎮 Future Improvements

After completing the basic version, the project can be expanded with real gameplay data.

Possible improvements:

* Collect data directly from a Unity game.
* Store player statistics in a database.
* Train the model using real player data.
* Compare different Machine Learning algorithms.
* Predict player performance.
* Predict whether a player will win or lose.
* Dynamically adjust game difficulty using the model.
* Deploy the model as an API.
* Connect the trained model with Unity.

### Possible Future Architecture

```text
Unity Game
    ↓
Player Gameplay Data
    ↓
Backend / Dataset
    ↓
Machine Learning Model
    ↓
Prediction
    ↓
Unity Game
```

## 📚 Learning Objective

This project is primarily a **learning project**.

The goal is not to build the most accurate score predictor, but to understand how a Machine Learning model is created, trained, evaluated, and used for predictions.

After completing this project, the next step will be to move from traditional Machine Learning to **Neural Networks and PyTorch**.

## 📝 License

This project is created for educational purposes.
