
import streamlit as st
import pandas as pd
import joblib


st.title("🎮 Game Player Score Predictor")
st.write("Enter the gameplay stats below and I'll predict the score.")


play_time = st.number_input("Play Time (Second)", 0, 300, 60)
enemies   = st.number_input("Enemies Killed", 0, 100, 12)
damage    = st.number_input("Damage Taken", 0, 500, 25)
balls     = st.number_input("Balls Collected", 0, 100, 8)


model = joblib.load("models/score_model.pkl")


player = pd.DataFrame([{
    "play_time": play_time,
    "enemies_killed": enemies,
    "damage_taken": damage,
    "balls_collected": balls
}])


if st.button("Predict Score"):
    result = model.predict(player)[0]
    st.success(f"Predicted Score: {result:.1f}")