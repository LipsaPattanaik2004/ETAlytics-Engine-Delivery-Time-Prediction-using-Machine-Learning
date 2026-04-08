import joblib
import pandas as pd

model = joblib.load('../model.pkl')

def predict_delivery(input_data):
    df = pd.DataFrame([input_data])
    df = pd.get_dummies(df)

    prediction = model.predict(df)
    return prediction[0]

if __name__ == "__main__":
    sample = {
        "distance_km": 5,
        "order_load": 10,
        "traffic_level_medium": 1,
        "weather_rainy": 1
    }

    print("Predicted Delivery Time:", predict_delivery(sample))
