import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from config import BASE_DIR, API

def get_data(pnu: str, year: int):
    param = {
        "key": API.LAND_API_KEY,
        "format": "json",
        "numOfRows": "100",
        "pageNo": "1",
        "pnu": pnu,
        "stdrYear": year
    }
    request_data = requests.get(API.LAND_FEATURE_URL, params=param)
    request = request_data.json()
    if "landCharacteristicss" in request:
        return request["landCharacteristicss"]["field"][0]
    else:
        return None
    
get_data("4413133028200240005", 2022)