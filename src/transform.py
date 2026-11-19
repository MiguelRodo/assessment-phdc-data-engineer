import pandas as pd

def count_by_suburb(data, file_path):
    data_by_suburb = data.groupby("C3_Suburb").size().reset_index(name = "Count").sort_values(ascending=False)
    data_by_suburb.to_csv(file_path, index=False)
    return file_path

def examine_suburb_field(data, file_path):
    return None

def read_raw_data(file_path="data/raw/extracted_data.csv"):
    return pd.read_csv(file_path)