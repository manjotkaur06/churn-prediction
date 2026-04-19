# 🔁 Customer Churn Prediction — End-to-End ML Project

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)
![Gradio](https://img.shields.io/badge/UI-Gradio-purple)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

> **Predict which telecom customers will churn — before they do.**
> Built as a full ML project covering EDA, Feature Engineering, Model Building, and Deployment with an interactive UI.

---

## 🌐 Live Demo

👉http://127.0.0.1:7860



---

## 📌 Problem Statement

A telecom company loses **26% of its customers every quarter**.
Acquiring a new customer costs **4x more** than retaining one.

🎯 **Goal:** Predict customers likely to churn so retention teams can act early.

---

## 🧠 Solution Overview

* Performed **EDA & feature engineering**
* Built multiple models and selected **XGBoost**
* Handled class imbalance using **SMOTE**
* Deployed using **Gradio UI for real-time predictions**

---

## 🗂️ Project Structure

```
churn-prediction/
│
├── app/
│   └── app.py              # Gradio UI + prediction logic
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── data/
├── requirements.txt
└── README.md
```

---

## 🔍 Key Insights (EDA)

| Insight                                   | Business Action       |
| ----------------------------------------- | --------------------- |
| Month-to-month customers churn at **42%** | Push annual contracts |
| First-year customers most risky           | Loyalty onboarding    |
| High charges + low tenure → high churn    | Offer discounts       |
| No tech support → higher churn            | Improve support       |

---

## ⚙️ Feature Engineering

* Tenure segmentation
* Total services count
* Average monthly value
* High-risk rule-based flag

---

## 🤖 Model Performance

| Model               | ROC-AUC  | Recall   |
| ------------------- | -------- | -------- |
| Logistic Regression | 0.78     | 0.61     |
| Random Forest       | 0.82     | 0.71     |
| **XGBoost (Final)** | **0.86** | **0.79** |

---

## 📏 Metrics Used

* ROC-AUC → ranking ability
* Recall → catch churners
* Precision → reduce false alarms
* F1 Score → balance

---

## 💰 Business Impact

* ~1,484 churners identified
* ₹26+ Lakhs potential net savings
* Enables targeted retention strategy

---

## 🚀 How to Run

```bash
git clone <repo-link>
cd churn-prediction
pip install -r requirements.txt
cd app
python app.py
```

👉 Open:
 http://127.0.0.1:7860

---

## ⚠️ Key Challenge 

❌ Model expected **30 features**, but UI provided only **3**

### ✅ Solution:

* Loaded `columns.pkl`
* Reconstructed full feature vector
* Applied `scaler.pkl`



---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Gradio

---

## 🔮 Future Improvements

* Full feature UI (gender, contract, etc.)
* Model explainability (SHAP)
* Cloud deployment
* Pipeline-based inference

---

## 🙋‍♀️ Author

**Manjot Kaur**

---

## ⭐ If you like this project

Give it a ⭐ and feel free to connect!
