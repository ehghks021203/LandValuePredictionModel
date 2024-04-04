import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from config import API

def get_by_region(ld_code: str, year: int, month: int):
    param = {
        "key": API.LAND_API_KEY,
        "format": "json",
        "numOfRows": "100",
        "pageNo": "1",
        "reqLdCode": ld_code,
        "stdrYear": year,
        "stdrMt": "{:02d}".format(month),
        "scopeDiv": "A"
    }
    request_data = requests.get(API.FLUCTUATION_RATE_OF_LAND_PRICE_BY_RIGION_URL, params=param)
    request = request_data.json()
    return request["byRegions"]["field"][0]

def get_by_zoning(ld_code: str, year: int, month: int):
    param = {
        "key": API.LAND_API_KEY,
        "format": "json",
        "numOfRows": "100",
        "pageNo": "1",
        "reqLdCode": ld_code,
        "stdrYear": year,
        "stdrMt": "{:02d}".format(month),
        "scopeDiv": "A"
    }
    param.setdefault("reqLdCode", ld_code)
    param.setdefault("stdrYear", str(year))
    param.setdefault("stdrMt", "{:02d}".format(month))
    param.setdefault("scopeDiv", "A")
    request_data = requests.get(API.FLUCTUATION_RATE_OF_LAND_PRICE_BY_ZONING_URL, params=param)
    request = request_data.json()
    return request["byZonings"]["field"][0]

def get_by_land_category(ld_code: str, year: int, month: int):
    param = {
        "key": API.LAND_API_KEY,
        "format": "json",
        "numOfRows": "100",
        "pageNo": "1",
        "reqLdCode": ld_code,
        "stdrYear": year,
        "stdrMt": "{:02d}".format(month),
        "scopeDiv": "A"
    }
    param.setdefault("reqLdCode", ld_code)
    param.setdefault("stdrYear", str(year))
    param.setdefault("stdrMt", "{:02d}".format(month))
    param.setdefault("scopeDiv", "A")
    request_data = requests.get(API.FLUCTUATION_RATE_OF_LAND_PRICE_BY_LAND_CATEGORY_URL, params=param)
    request = request_data.json()
    return request["byLandCategorys"]["field"][0]

def get_large_cl_by_region(ld_code: str, year: int, month: int):
    param = {
        "key": API.LAND_API_KEY,
        "format": "json",
        "numOfRows": "100",
        "pageNo": "1",
        "stdrYear": year,
        "stdrMt": "{:02d}".format(month),
        "scopeDiv": "A"
    }
    request_data = requests.get(API.FLUCTUATION_RATE_OF_LAND_PRICE_LARGE_CL_BY_RIGION_URL, params=param)
    request = request_data.json()
    for data in request["byRegions"]["field"]:
        if data["ldCtprvnCode"] == ld_code[0:2]:
            return data
    return None
