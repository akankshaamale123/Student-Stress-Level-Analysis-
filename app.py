{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15595ea4-7176-4d00-af48-f0b2a44735f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load your trained stacking model and scaler\n",
    "with open(\"stacking_model.pkl\", \"rb\") as model_file:\n",
    "    model = pickle.load(model_file)\n",
    "\n",
    "with open(\"scaler.pkl\", \"rb\") as scaler_file:\n",
    "    scaler = pickle.load(scaler_file)\n",
    "\n",
    "# Streamlit app title\n",
    "st.set_page_config(page_title=\"Student Stress Level Prediction\", page_icon=\"🧠\")\n",
    "st.title(\"🧠 Student Stress Level Analysis App\")\n",
    "st.write(\"Enter the details below to predict your stress level:\")\n",
    "\n",
    "# Collect user input\n",
    "study_hours = st.number_input(\"📘 Study Hours Per Day\", min_value=0.0, max_value=24.0, step=0.5)\n",
    "extra_hours = st.number_input(\"🎭 Extracurricular Hours Per Day\", min_value=0.0, max_value=24.0, step=0.5)\n",
    "sleep_hours = st.number_input(\"😴 Sleep Hours Per Day\", min_value=0.0, max_value=24.0, step=0.5)\n",
    "social_hours = st.number_input(\"👥 Social Hours Per Day\", min_value=0.0, max_value=24.0, step=0.5)\n",
    "physical_hours = st.number_input(\"🏃 Physical Activity Hours Per Day\", min_value=0.0, max_value=24.0, step=0.5)\n",
    "gpa = st.number_input(\"🎓 GPA\", min_value=0.0, max_value=10.0, step=0.1)\n",
    "academic_performance = st.number_input(\"📊 Academic Performance (Encoded)\", min_value=0, max_value=5, step=1)\n",
    "\n",
    "# Button for prediction\n",
    "if st.button(\"🔍 Predict Stress Level\"):\n",
    "    # Prepare input data\n",
    "    input_data = np.array([[study_hours, extra_hours, sleep_hours, social_hours,\n",
    "                            physical_hours, gpa, academic_performance]])\n",
    "\n",
    "    # Scale the input using the same scaler used during training\n",
    "    scaled_input = scaler.transform(input_data)\n",
    "\n",
    "    # Make prediction\n",
    "    prediction = model.predict(scaled_input)\n",
    "\n",
    "    # Map the prediction to stress levels\n",
    "    stress_levels = {0: \"😌 Low Stress\", 1: \"😐 Medium Stress\", 2: \"😣 High Stress\"}\n",
    "    result = stress_levels.get(prediction[0], \"Unknown\")\n",
    "\n",
    "    # Display result\n",
    "    st.success(f\"Predicted Stress Level: {result}\")\n",
    "\n",
    "# Optional footer\n",
    "st.markdown(\"---\")\n",
    "st.caption(\"Developed by Akanksha | Student Stress Analysis Project 💻\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
