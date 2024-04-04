import requests
import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from config import BASE_DIR, API

STT_LAT = 35.14201677983137
STT_LNG = 126.84330326366048
END_LAT = 37.72912760937938
END_LNG = 129.0891177737519
BBOX_SIZE = 0.01
DATA_PATH = f"{BASE_DIR}/Data/"
SAVE_PATH = f"{BASE_DIR}/.crawling_land_data_with_place.bp"

def get_break_point() -> tuple:
    if os.path.isfile(SAVE_PATH):
        bp_f = open(SAVE_PATH, "r")
        data = bp_f.readline().split(",")
        lat = float(data[0])
        lng = float(data[1])
        bp_f.close()
    else:
        bp_f = open(SAVE_PATH, "w")
        bp_f.write("{},{}".format(STT_LAT, STT_LNG))
        bp_f.close()
        lat = STT_LAT
        lng = STT_LNG
    return lat, lng

def save_break_point(lat: float, lng: float) -> None:
    bp_f = open(SAVE_PATH, "w")
    bp_f.write("{},{}".format(lat, lng))
    bp_f.close()

def save_crawling_data(data: dict, file_path: str) -> None:
    if not os.path.isfile(DATA_PATH + file_path):
        csv_f = open(DATA_PATH + file_path, "w")
        csv_w = csv.writer(csv_f)
        csv_w.writerow(data.keys())
        csv_f.close()
    csv_f = open(DATA_PATH + file_path, "a")
    csv_w = csv.writer(csv_f)
    csv_w.writerow(data.values())
    csv_f.close()

def next_step(lat: float, lng: float):
    if lat < END_LAT:
        lat += BBOX_SIZE
    elif lng < END_LNG:
        lat = STT_LAT
        lng += BBOX_SIZE
    else:
        sys.exit()
    return lat, lng

def get_crawling_data(lat: float, lng: float) -> list:
    return_list = []
    a = "{:2.16f}".format(lat)
    b = "{:2.16f}".format(lng)
    c = "{:2.16f}".format(lat + BBOX_SIZE)
    d = "{:2.16f}".format(lng + BBOX_SIZE)
    clat = "{:2.16f}".format((lat*2 + BBOX_SIZE)/2)
    clng = "{:2.16f}".format((lng*2 + BBOX_SIZE)/2)
    url = API.create_land_price_url(a, b, c, d, clat, clng)
    request_data = requests.get(url)
    request = request_data.json()
    for req in request:
        return_dict = {"PNU":req["pnu"],"Year":req["y"][0:4],"Month":str(int(req["y"][4:6])),"Price":req["p"],"DealArea":req["la"]}
        # return_str = "{},{},{},{},{}".format(req["pnu"], int(req["y"][0:4]), int(req["y"][4:6]), req["p"], req["la"])
        # print(return_str)
        return_list.append(return_dict)
    return return_list
