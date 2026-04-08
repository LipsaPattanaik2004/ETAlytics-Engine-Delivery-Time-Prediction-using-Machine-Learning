def create_features(df):
    df['distance_per_order'] = df['distance_km'] / (df['order_load'] + 1)
    return df
