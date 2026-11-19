import pandas as pd
from pathlib import Path

def count_by_suburb(data, file_path = Path("data/output/grouped_by_suburb.csv")):
    data_by_suburb = data.groupby("Suburb").size().reset_index(name = "Count").sort_values("Count", ascending=False)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    data_by_suburb.to_csv(file_path, index=False)
    return file_path

def examine_suburb_field(data, file_path):
    data_suburb = data["Suburb"]
    data_suburb = data_suburb.str.lower().str.strip()
    data_suburb_unique = data_suburb.drop_duplicates()
    return None

def read_raw_data(file_path="data/raw/extracted_data.csv"):
    return pd.read_csv(file_path)