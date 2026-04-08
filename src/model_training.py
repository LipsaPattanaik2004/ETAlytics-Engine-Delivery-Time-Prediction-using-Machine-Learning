import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

from data_preprocessing import load_data, encode_features
from feature_engineering import create_features

def train_model():
    df = load_data('../data/delivery_data.csv')
    df = encode_features(df)
    df = create_features(df)

    X = df.drop('delivery_time', axis=1)
    y = df['delivery_time']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    joblib.dump(model, '../model.pkl')

    print("Model trained and saved!")

if __name__ == "__main__":
    train_model()
