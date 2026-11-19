from pathlib import Path

import requests
import pandas as pd

timeout=5

def extract_page(url, timeout=5):
  response = requests.get(
    url,
    timeout=timeout,
    params = {"f": "json", "where": "C3_Complaint_type = 'No Power'", "OutFields": "*"}
  )
  response.raise_for_status()
  data = response.json()
  features = data["features"]
  df = pd.DataFrame([feature["attributes"] for feature in features])
  return response.text
