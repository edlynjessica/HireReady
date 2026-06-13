# 🚀 HireReady – ML-Based Student Placement Predictor

HireReady is a machine learning-powered web application that evaluates a student's job readiness based on academic performance, coding skills, projects, internships, and communication abilities.

It generates a **HireReady Score (0–100)** along with personalized feedback, strengths, weaknesses, and actionable improvement suggestions.

---

## ✨ Features

- 🔐 User Authentication (Sign Up / Login using SQLite)
- 🧠 ML-based HireReady Score prediction
- 💻 DSA profile breakdown (LeetCode Easy / Medium / Hard)
- 🏗️ Project & Internship evaluation
- 💬 Communication skill assessment
- 📊 Real-time profile insights
- 🚀 Personalized improvement suggestions
- 🎯 Interactive Streamlit dashboard UI

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Regressor
- **Trained on:** Synthetic student dataset
- **Target:** HireReady Score (0–100)

### 📌 Input Features:
- CGPA  
- LeetCode Easy / Medium / Hard  
- Contest Rating  
- Projects  
- Internships  
- Communication Skills  

---

## 🗂️ Project Structure

    HireReady/
    │
    ├── app.py # Streamlit frontend
    ├── database.py # SQLite authentication system
    ├── ml_model.py # Model training script
    ├── model.pkl # Trained ML model
    ├── generate_dataset.py # Synthetic dataset generator
    ├── synthetic_students.csv
    ├── hireready.db
    ├── requirements.txt
    └── README.md

---

## 🌐 Live Demo

    https://hireready-ml.streamlit.app/
    
---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

--- 

## 📦 Requirements

* streamlit
* pandas
* scikit-learn
* bcrypt

---

## 🎯 Sample Output

After submitting the assessment, the system generates:

- 🎯 HireReady Score (0–100)

### 💪 Strengths:
- Strong DSA profile  
- Good project experience  

### 📌 Weaknesses:
- Improve consistency in DSA  
- Build more real-world projects  

### 🚀 Action Plan:
- Solve 2–3 LeetCode problems daily  
- Build and deploy full-stack projects  
- Apply for internships actively  

---

## 💡 Future Improvements

- 🔗 Integrate Codolio API for automatic data fetching  
- 📈 Improve ML model accuracy with real datasets  
- ☁️ Deploy on AWS / Streamlit Cloud  
- 🧾 Add Resume Analyser
- 📊 Add advanced analytics dashboard  

---

## 👨‍💻 Author

**Edlyn Jessica Philip**  
B.E CSE | Student Developer 

---

## ⭐ Note

This project is part of an end-to-end ML learning journey covering:

- Data generation  
- Model training  
- Web app deployment  
- Full-stack integration  
