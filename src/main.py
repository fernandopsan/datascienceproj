import pandas as pd
import common.tools as tools
import model.model as model
import visualization.visualize as visualize
import  preprocess.prepare_data as pre
import yaml as ym

def load_config():
    print('Loading configs...')
    config = tools.load_config()
    with open('../config.yaml') as p:
        config = ym.safe_load(p)
    return config

def load_data(config):
    print('Loading data...')
    df = pd.read_csv(config["datalink"])
    return df

def pre_process_data(config):    
    df = load_data(config)
    print("Pre processing data...")
    df = pre.convert_meterno_to_string(df)
    df = pre.cast_and_rename_columns(df)
    df = pre.process_missing_values(df, columns=["PUBLISHEDPACKET", "GAPREQPACKET"], processing_method="replace", value=0)
    df = pre.create_gapreq_efficiency_column(df)
    df = pre.create_information_columns(df)    
    return df

def start_process():
    print('Starting process..')
    config = load_config()
    print("Data path:", config['datalink'])
    df = pre_process_data(config)
    start_model(df)

def start_model(df):    
    print('Starting the model process...')
    df_model = model.prepare_data(df)
    X, y = model.prepare_features(df_model)

    X_train, y_train, X_test, y_test = model.split_data_in_test_and_train(df_model)

    lrModel = model.train_model(X_train, y_train)

    y_pred_train, y_pred_test = model.test_model(lrModel, X_train, X_test)    

    mse, mae, r2 = visualize.evaluate_model(y_test, y_pred_test)

    visualize.print_results(mse, mae, r2, y_test, y_pred_test)


start_process()