import pandas as pd
import numpy as np
from typing import List
import yaml as ym

def load_config():
    # Read in the configuration file
    with open('../config.yaml') as p:
        config = ym.safe_load(p)
    return config

def cast_and_rename_columns(dataframe):
    dataframe["INTERVALDATE"] = pd.to_datetime(
        dataframe["INTERVALDATE"]
    )
    columns_mapping = {
        "'Published Packet'": "PUBLISHEDPACKET",
        "'Gap Analysis Packet'": "GAPREQPACKET",
    }
    dataframe = dataframe.rename(columns=columns_mapping)
    return dataframe
    
def process_missing_values(
    dataframe: pd.DataFrame,
    columns: List[str],
    processing_method: str = "remove",
    how: str = "any",
    value: int = -1000,
    order_by: str = "Data Hora",
):

    if processing_method == "remove":
        return dataframe.dropna(subset=columns, how=how)

    if processing_method == "replace":
        dataframe[columns] = dataframe[columns].fillna(value)
        return dataframe

    dataframe = dataframe.sort_values(order_by)

    if processing_method == "forward":
        dataframe[columns] = dataframe[columns].ffill()

    elif processing_method == "backward":
        dataframe[columns] = dataframe[columns].bfill()

    elif processing_method == "both":
        dataframe[columns] = dataframe[columns].ffill().bfill()

    else:
        raise ValueError(
            f"Processing method '{processing_method}' not implemented."
        )
    return dataframe

def create_information_columns(dataframe):
    dataframe["TOTALINTERVALS"] = (
        dataframe["PUBLISHEDPACKET"]
        + dataframe["GAPREQPACKET"]
    )
    dataframe["INFORMATION"] = np.where(
        dataframe["TOTALINTERVALS"] == 288,
        "Complete",
        "Incomplete",
    )
    dataframe["INFORMATIONPERCENT"] = (
        (dataframe["TOTALINTERVALS"] / 288) * 100
    ).round(2)
    return dataframe

def create_gapreq_efficiency_column(dataframe):
    dataframe["GAPREQEFFICIENCY"] = (
        (
            dataframe["GAPREQPACKET"]
            / (288 - dataframe["PUBLISHEDPACKET"])
        ) * 100
    ).round(2)
    return dataframe