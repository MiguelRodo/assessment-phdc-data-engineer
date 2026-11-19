import logging
import time
from pathlib import Path

import pandas as pd
import requests

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

timeout = 5

def log_n_records_total(url, timeout, params):
  count_data = extract_json(
    url,
    timeout=timeout,
    params={
        "f": "json",
        "where": params["where"],
        "returnCountOnly": "true",
    }
  )
  expected_count = count_data["count"]
  logger.info("ArcGIS reports %d matching rows", expected_count)
  return expected_count

def extract_attributes(data):
    features = data["features"]
    return pd.DataFrame([feature["attributes"] for feature in features])

def extract_json(url, timeout, params):
    n_try = 0
    while n_try < 3:
        n_try += 1
        try:
            response = requests.get(
                url, timeout=timeout + timeout * (n_try - 1) * 2, params=params
            )
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if n_try >= 3:
                raise
            logger.warning(f"Attempt {n_try} failed: {e}")
            time.sleep(5 * n_try)
            continue
        break
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise ValueError(f"Error in response: {data['error']}")
    return data


def get_returned_all(data):
    return not data.get("exceededTransferLimit", False)


def save_csv(df, file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)
    logger.info("Saved %d rows to %s", len(df), file_path)
    return file_path

def extract_records(url, timeout=5, page_size=1000, max_records=None, file_path="data/raw/extracted_data.csv"):
    params_base = {
        "f": "json",
        "where": "C3_Complaint_Type = 'No Power'",
        "outFields": "*",
        "resultRecordCount": page_size,
    }
    expected_count = log_n_records_total(url, timeout, params_base)
    data = extract_json(url, timeout=timeout, params=params_base)
    pages = [extract_attributes(data)]
    fetched = len(pages[0])
    if max_records is not None and fetched >= max_records:
        pages[0] = pages[0].head(max_records)
        return save_csv(pd.concat(pages, ignore_index=True), file_path)
    offset = 0
    logger.info("Fetched %d / %d rows (offset %d)", fetched, expected_count, offset)
    returned_all = get_returned_all(data)
    while not returned_all:
        offset += page_size
        params_loop = params_base.copy()
        params_loop["resultOffset"] = offset
        data = extract_json(url, timeout=timeout, params=params_loop)
        page = extract_attributes(data)
        pages.append(page)
        fetched += len(page)
        if max_records is not None and fetched >= max_records:
          pages[-1] = pages[-1].head(max_records - (fetched - len(page)))
          return save_csv(pd.concat(pages, ignore_index=True), file_path)
        logger.info("Fetched %d / %d rows (offset %d)", fetched, expected_count, offset)
        returned_all = get_returned_all(data)
    df = pd.concat(pages, ignore_index=True)
    if len(df) != expected_count:
        raise ValueError(f"Fetched {len(df):,} rows, expected {expected_count:,}")
    logger.info(f"Extracted {len(df)} records")
    save_csv(df, file_path)
    return file_path
