import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

def prepare_data(df):
    df_1 = df
    df_1 = df_1.drop(columns=['METERNO'])
    df_1 = df_1.drop(columns=['METERID'])
    df_1 = df_1.drop(columns=['INTERVALDATE'])
    df_1 = df_1.drop(columns=['INFORMATION'])
    df_1['DAY'] = df['INTERVALDATE'].dt.day
    df_1['MONTH'] = df['INTERVALDATE'].dt.month
    df_1['YEAR'] = df['INTERVALDATE'].dt.year
    df_1['GAPREQEFFICIENCY'] = df_1['GAPREQEFFICIENCY'].fillna(0)
    return df_1

def prepare_features(df):
    #Prepare features (X) and target (y)
    X = df[['ENDPOINTID', 'DAY', 'MONTH', 'YEAR', 'INTERVALCHANNELNO', 'PUBLISHEDPACKET', 'GAPREQPACKET', 'TOTALINTERVALS', 'INFORMATIONPERCENT']]
    y = df['GAPREQEFFICIENCY']
    return X, y

def split_data_in_test_and_train(df):
    # Split the data into train and test sets
    train_data = df.sample(frac=0.9, random_state=42)  # 90% training
    test_data = df.drop(train_data.index)             # 10% testing

    X_train = train_data[['ENDPOINTID', 'DAY', 'MONTH', 'YEAR', 'INTERVALCHANNELNO', 'PUBLISHEDPACKET', 'GAPREQPACKET', 'TOTALINTERVALS', 'INFORMATIONPERCENT']]
    y_train = train_data['GAPREQEFFICIENCY']

    X_test = test_data[['ENDPOINTID', 'DAY', 'MONTH', 'YEAR', 'INTERVALCHANNELNO', 'PUBLISHEDPACKET', 'GAPREQPACKET', 'TOTALINTERVALS', 'INFORMATIONPERCENT']]
    y_test = test_data["GAPREQEFFICIENCY"]

    return X_train, y_train, X_test, y_test

def train_model(X_train, y_train):
    # Train the model    
    model = RandomForestRegressor(
        n_estimators=100,      # Number of trees in the forest
        max_depth=None,        # Trees expand until leaves are pure
        min_samples_split=2,   # Minimum samples required to split a node
        random_state=42,       # Ensures reproducible results
        n_jobs=-1              # Use all available CPU cores for parallel processing
    )

    model.fit(X_train, y_train)    
    return model

def test_model(model, X_train, X_test):
    # Test the model
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    return y_pred_train, y_pred_test    