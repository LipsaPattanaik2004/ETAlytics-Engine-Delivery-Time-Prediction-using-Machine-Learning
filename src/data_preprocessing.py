import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def encode_features(df):
    df = pd.get_dummies(df, columns=['traffic_level', 'weather'])
    return df
