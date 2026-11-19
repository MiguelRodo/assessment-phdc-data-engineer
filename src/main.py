
import extract

if __name__ == "__main__":
  url = "https://services6.arcgis.com/nyYfO9SxHU2ChQd9/arcgis/rest/services/Service_Requests_2023_until_20_May_2026/FeatureServer/0/query"
  path_records = extract.extract_records(url)
