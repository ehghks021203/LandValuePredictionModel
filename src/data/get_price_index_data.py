import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from config import API

def get_producer_price_index_data(year: int, month: int) -> float:
    request_data = requests.get(API.create_producer_price_index_url(year, month))
    request = request_data.json()
    if "StatisticSearch" in request:
        return float(request["StatisticSearch"]["row"][0]["DATA_VALUE"])
    else:
        return None

def get_consumer_price_index_data(year: int, month: int) -> float:
    request_data = requests.get(API.create_consumer_price_index_url(year, month))
    request = request_data.json()
    if "StatisticSearch" in request:
        return float(request["StatisticSearch"]["row"][0]["DATA_VALUE"])
    else:
        return None


if __name__ == "__main__":
    print("input year >> ", end="")
    year = int(input())
    print("input month >> ", end="")
    month = int(input())
    ppi = get_producer_price_index_data(year, month)
    cpi = get_consumer_price_index_data(year, month)
    print("ppi: {:.2f}\ncpi: {:.2f}".format(ppi, cpi))