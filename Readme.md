# Fake News Detector

## Project Overview

Fake News Detector is a Machine Learning based web application that detects whether a news article is Fake or Real using Natural Language Processing (NLP) techniques.

This project uses:

* TF-IDF Vectorization
* Logistic Regression
* Streamlit Web Application

---

# Features

* Detects Fake and Real News
* NLP-based text preprocessing
* Machine Learning classification
* Streamlit interactive web application
* Real-time prediction system

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* NLP Techniques

---

# Dataset

Dataset used:

* Fake.csv
* True.csv

The dataset contains real and fake news articles used for training the machine learning model.

---

# Project Workflow

Dataset Collection
↓
Data Cleaning
↓
EDA (Exploratory Data Analysis)
↓
Text Preprocessing
↓
TF-IDF Vectorization
↓
Machine Learning Model
↓
Model Evaluation
↓
Prediction System
↓
Streamlit Deployment

---

# Machine Learning Model

Model Used:

* Logistic Regression

Vectorization Technique:

* TF-IDF Vectorizer

---

# Model Performance

The model achieves high accuracy on the fake news dataset and performs real-time predictions efficiently.

---

# Project Structure

```text id="pc28ac"
Fake_News_Detector/
│
├── app.py
├── fake_news_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── Fake_News_Detector.ipynb
```

---

# Run Locally

## Install Requirements

```bash id="iiwidi"
pip install -r requirements.txt
```

## Run Streamlit App

```bash id="emz1rk"
streamlit run app.py
```

---

# Deployment

The project is deployed using Streamlit Cloud.

---

# Application Features

* News article input
* Fake/Real prediction
* Interactive user interface
* Fast response time

---

# Author

Anis

---

# Future Improvements

* Deep Learning integration
* BERT model implementation
* News source verification
* Confidence score visualization
* Multi-language fake news detection
