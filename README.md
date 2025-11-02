🧠 Student Stress Level Analysis using Machine Learning
  🎓 A Machine Learning & Data Science project designed to analyze and predict student stress levels based on academic, lifestyle, and personal habits.
  
  
🌟 Project Overview
- Student mental health is one of the most important issues in today’s education system.
- This project aims to predict stress levels (Low, Moderate, High) among students using supervised machine learning models.
- It analyzes daily habits such as study hours, sleep, social activities, and academic performance to identify potential stress indicators.
  

🎯 Objectives
- Understand how lifestyle and academic factors influence stress levels.
- Build an accurate predictive model for classifying student stress.
- Compare multiple ML algorithms and select the best performer.
- Provide an interactive Streamlit app for real-time stress prediction.
  

📊 Dataset Information

| Feature Type       | Description                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| 🎯 **Target**      | `Stress_Level` → {Low, Moderate, High}                                                                      |
| 📁 **Features**    | Study Hours, Sleep Hours, Extracurricular Hours, Social Hours, Physical Activity, GPA, Academic Performance |
| 🔢 **Records**     | ~2000+ student records                                                                                      |
| 🧩 **File Format** | CSV                                                                                                         |


🧹 Data Preprocessing Steps

- Removed duplicates and handled missing values.
- Dropped irrelevant columns like Student_ID.
- Encoded target variable: Low → 0, Moderate → 1, High → 2.
- Scaled features using StandardScaler or RobustScaler to reduce outlier impact.
- Performed train-test split (80–20 ratio).


📈 Exploratory Data Analysis (EDA)

Visualizations performed:
- Histograms & KDE plots (Feature distributions)
- Boxplots (Outlier detection)
- Correlation Heatmap
- Pairplots for multi-feature relationships

🔍 Key Insights:
- High academic load → higher stress probability.
- More sleep → lower stress levels.
- Physical activity significantly reduces stress risk.

  

🤖 Machine Learning Models Used

| Model               | Type          | Accuracy          | Remark                               |
| ------------------- | ------------- | ----------------- | ------------------------------------ |
| Logistic Regression | Linear        | ⭐ Good baseline  | Simple & interpretable               |
| Decision Tree       | Non-linear    | 🌿 Moderate       | Handles non-linearity                |
| Random Forest       | Ensemble      | 🏆 Excellent      | Robust & accurate                    |
| Stacking Classifier | Meta Ensemble | 💡 Best Performer | Combines multiple models effectively |



🧮 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Curve

 
🏆 Results Summary

- The Stacking Classifier achieved the highest accuracy (~95%).
- Balanced recall across all stress levels.
- Feature importance shows sleep hours and academic performance as key predictors.
  

📊 Example Model Accuracy:
- Logistic Regression → 82%
- Decision Tree → 85%
- Random Forest → 92%
- Stacking Classifier → 95%
  


💻 Tech Stack

| Category       | Tools / Libraries                                |
| -------------- | ------------------------------------------------ |
| 🐍 Language    | Python                                           |
| 📚 Libraries   | Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn |
| 🧰 Environment | Jupyter Notebook                                 |
| 🚀 Deployment  | Streamlit                                        |

🚀 How to Run

# Clone the repo
git clone https://github.com/akankshaamale123/Student-Stress-Level-Analysis-.git

# Navigate to folder
cd Student-Stress-Level-Analysis-

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook Project Student Stress.ipynb



🔮 Future Enhancements

- Integrate SHAP/LIME for model explainability.
- Build an analytics dashboard to visualize patterns.
- Collect more real-world student survey data.
- Enhance the UI with charts and recommendations.
  
  

👩‍💻 Author

Akanksha Amale
Data Science & Machine Learning Enthusiast
💬 Passionate about using data to understand human behavior and mental well-being.


📧 Contact: akankshaamale@gmail.com


🌈 "Smart predictions for a healthier, balanced student life."
