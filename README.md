# Heart Disease Prediction using Machine Learning

## Project Overview

This project is a Machine Learning-based Heart Disease Prediction System that predicts the likelihood of heart disease using patient health-related parameters.

Multiple classification algorithms were implemented and compared. Random Forest was selected for the final Flask-based web application.

## Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Data visualization using Matplotlib and Seaborn
- Implementation of multiple classification algorithms
- Model performance comparison
- Random Forest-based prediction
- Prediction probability using `predict_proba()`
- Flask web application for real-time predictions
- User-friendly HTML/CSS interface

## Machine Learning Models

The following classification algorithms were implemented:

- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest

## Model Evaluation

The models were evaluated using Accuracy, Precision, Recall, F1-Score, and ROC-AUC.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 78.69% | 76.32% | 87.88% | 81.69% | 86.47% |
| Decision Tree | 72.13% | 71.05% | 81.82% | 76.06% | 71.27% |
| KNN | 80.33% | 76.92% | 90.91% | 83.33% | 86.74% |
| Random Forest | 78.69% | 75.00% | 90.91% | 82.19% | 87.82% |

## Input Features

The application uses 13 input features:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression (Oldpeak)
- ST Segment Slope
- Number of Major Vessels (CA)
- Thalassemia

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Joblib
- HTML
- CSS

## Project Structure

```text
Heart-Disease/
│
├── dataset/
│   └── heart.csv
│
├── model/
│   ├── knn_model.pkl
│   ├── random_forest_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── heart_disease.ipynb
│
├── static/
│
├── templates/
│   └── index.html
│
├── app.py
├── README.md
└── requirements.txt