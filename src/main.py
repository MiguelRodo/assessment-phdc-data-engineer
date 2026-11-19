from pathlib import Path

import extract
import transform

if __name__ == "__main__":
  url = "https://services6.arcgis.com/nyYfO9SxHU2ChQd9/arcgis/rest/services/Service_Requests_2023_until_20_May_2026/FeatureServer/0/query"

  path_records = Path("data/raw/extracted_data.csv")
  extract.extract_records(url, timeout=30, max_records=None, file_path=path_records)
  raw_data = transform.read_raw_data(path_records)
  transform.count_by_suburb(raw_data)


  
