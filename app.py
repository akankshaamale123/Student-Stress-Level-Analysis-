import streamlit as st
import pickle
import numpy as np

# Load your trained stacking model and scaler
with open("stacking_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit app title
st.set_page_config(page_title="Student Stress Level Prediction", page_icon="🧠")
st.title("🧠 Student Stress Level Analysis App")
st.write("Enter the details below to predict your stress level:")

# Collect user input
study_hours = st.number_input("📘 Study Hours Per Day", min_value=0.0, max_value=24.0, step=0.5)
extra_hours = st.number_input("🎭 Extracurricular Hours Per Day", min_value=0.0, max_value=24.0, step=0.5)
sleep_hours = st.number_input("😴 Sleep Hours Per Day", min_value=0.0, max_value=24.0, step=0.5)
social_hours = st.number_input("👥 Social Hours Per Day", min_value=0.0, max_value=24.0, step=0.5)
physical_hours = st.number_input("🏃 Physical Activity Hours Per Day", min_value=0.0, max_value=24.0, step=0.5)
gpa = st.number_input("🎓 GPA", min_value=0.0, max_value=10.0, step=0.1)
academic_performance = st.number_input("📊 Academic Performance (Encoded)", min_value=0, max_value=5, step=1)

# Button for prediction
if st.button("🔍 Predict Stress Level"):
    # Prepare input data
    input_data = np.array([[study_hours, extra_hours, sleep_hours, social_hours,
                            physical_hours, gpa, academic_performance]])

    # Scale the input using the same scaler used during training
    scaled_input = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(scaled_input)

    # Map the prediction to stress levels
    stress_levels = {0: "😌 Low Stress", 1: "😐 Medium Stress", 2: "😣 High Stress"}
    result = stress_levels.get(prediction[0], "Unknown")

    # Display result
    st.success(f"Predicted Stress Level: {result}")

# Optional footer
st.markdown("---")
st.caption("Developed by Akanksha | Student Stress Analysis Project 💻")
