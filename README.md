# ETAlytics Engine - Delivery Time Prediction using Machine Learning

## Overview
ETAlytics Engine is a machine learning-based system designed to predict delivery time (ETA) for last-mile logistics. The project leverages key operational factors such as distance, traffic conditions, weather, and order load to estimate delivery duration accurately.

This project demonstrates end-to-end implementation of a predictive analytics pipeline, including data preprocessing, feature engineering, model training, and deployment via a REST API.

---

## Objectives
- Predict delivery time using real-world influencing factors
- Apply regression-based machine learning models
- Perform feature engineering to improve model performance
- Build a scalable and reusable prediction pipeline
- Deploy the model using a lightweight API

---

## Features
- Data preprocessing and encoding of categorical variables
- Custom feature engineering for enhanced prediction accuracy
- Machine learning model using Random Forest Regressor
- Model persistence using joblib
- REST API for real-time predictions using Flask
- Modular and maintainable project structure

---

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Flask
- Joblib

---

## Project Structure
ETAlytics-Engine/
│
├── data/
│   └── delivery_data.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── predict.py
│
├── app.py
├── requirements.txt
├── README.md

---

## Dataset Description
The dataset includes the following features:

- distance_km: Distance between store and delivery location
- traffic_level: Traffic conditions (low, medium, high)
- weather: Weather conditions (clear, rainy, foggy)
- order_load: Number of active orders at the time
- delivery_time: Actual delivery time (target variable)

---

## Installation and Setup

### Step 1: Clone the Repository
git clone https://github.com/your-username/ETAlytics-Engine.git

### Step 2: Navigate to Project Directory
cd ETAlytics-Engine

### Step 3: Install Dependencies
pip install -r requirements.txt

---

## Model Training

Run the following command to train the model:

python src/model_training.py

This will:
- Load and preprocess the dataset
- Perform feature engineering
- Train the Random Forest model
- Save the trained model as model.pkl

---

## Running the Application

Start the Flask API server:

python app.py

The API will run on:
http://127.0.0.1:5000

---

## API Usage

### Endpoint
POST /predict

### Sample Input (JSON)
{
    "distance_km": 5,
    "order_load": 10,
    "traffic_level_medium": 1,
    "weather_rainy": 1
}

### Sample Output
{
    "delivery_time": 32.5
}

---

## Machine Learning Approach

- Model Used: Random Forest Regressor
- Problem Type: Regression
- Feature Engineering:
  - Distance per order ratio
  - One-hot encoding of categorical variables
- Evaluation Strategy:
  - Train-test split

---

## Future Improvements
- Integrate XGBoost and LightGBM models
- Add model evaluation metrics such as RMSE and MAE
- Use real-world datasets for improved accuracy
- Implement hyperparameter tuning
- Deploy using Docker and cloud platforms (AWS/GCP)
- Add real-time data streaming capabilities

---

## Conclusion
ETAlytics Engine provides a practical implementation of delivery time prediction using machine learning. It reflects real-world challenges in last-mile logistics and demonstrates strong fundamentals in data science, feature engineering, and model deployment.

---

## Author
Lipsa Pattanaik
ITER SOA UNIVERSITY
