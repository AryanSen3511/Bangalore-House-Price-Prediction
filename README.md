# 🏠 Bangalore House Price Prediction

### A Machine Learning web application built using Flask, Scikit-Learn, and Pandas to predict housing prices in Bangalore based on input features like location, square feet area, BHK, and bathrooms.

---

## 📌 Project Goal

To create a real-time prediction system that allows users to estimate property prices in Bangalore using a trained regression model and a user-friendly web interface.

---

## 👀 Live UI Look

<img width="1117" height="836" alt="image" src="https://github.com/user-attachments/assets/518b42c0-a626-4d74-8e1e-2fabc0d1420e" />


---


## 🚀 Features

1. Predict house price in Bangalore
2. User-friendly web interface built using Flask
3. Model trained using Ridge Regression
4. Uses cleaned and processed housing dataset
5. Live form input for prediction
---

## 📁 Project Structure

```

📦 Bangalore-House-Price-Prediction
│
├── main.py                     # Flask application
├── Cleaned_data.csv            # Final cleaned dataset
├── RidgeModel.pkl              # Saved trained ML model
├── requirements.txt            # Required Python libraries
├── templates/
│     └── index.html            # Web UI
└── README.md                   # Project documentation

```


---


## 🧠 Model Training Summary

During model experimentation, three regression algorithms were evaluated:

```

No Regularization (Linear Regression): 0.82339
Lasso Regression:                     0.81282
Ridge Regression:                     0.82341  ✔ (Best model)

```

📍 Based on performance, Ridge Regression was selected and deployed.


---


## 💻 How to Run Locally

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Start the Flask App

```
python main.py
```

### 3️⃣ Open Browser

```
http://127.0.0.1:5081/
```

---

## 🛠️ Tech Stack

1. Python
2. Flask
3. Pandas
4. Scikit-Learn
5. HTML + Bootstrap


---


## 🧠 Model Details

1. Algorithm: Ridge Regression
2. Data cleaning performed using Pandas
3. One-hot encoding applied to categorical features
4. Model saved using pickle


---


## 💻 Author

Aryan Sen — Machine Learning


---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute this project, provided proper credit is given.



