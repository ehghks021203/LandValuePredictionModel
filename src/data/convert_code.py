import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from config import BASE_DIR

PLACE_CODE = {
    "MT1":"대형마트", 
    "CS2":"편의점", 
    "PS3":"어린이집 및 유치원", 
    "SC4":"학교", 
    "AC5":"학원", 
    "PK6":"주차장", 
    "OL7":"주유소 및 충전소", 
    "SW8":"지하철역", 
    "BK9":"은행",
    "CT1":"문화시설",
    "AG2":"중개업소",
    "PO3":"공공기관",
    "AT4":"관광명소",
    "AD5":"숙박",
    "FD6":"음식점",
    "CE7":"카페",
    "HP8":"병원",
    "PM9":"약국"
}


def code2addr(code: str):
    with open(BASE_DIR + "/Data/CodeData/PnuCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["sido"] + " " + d["sigungu"] + " " + d["eupmyeondong"] + " " + d["donglee"]

def code2regstr(code: str):
    with open(BASE_DIR + "/Data/CodeData/RegstrSeCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["kr-name"]

def code2lndcgr(code: str):
    with open(BASE_DIR + "/Data/CodeData/LandCgrCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["kr-name"]

def code2zoning(code: str):
    with open(BASE_DIR + "/Data/CodeData/LandZoningCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["kr-name"]

def code2landcategory(code: str):
    with open(BASE_DIR + "/Data/CodeData/LandCategoryCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["kr-name"]
        
def code2tpgrphfrm(code: str):
    with open(BASE_DIR + "/Data/CodeData/TpgrphFrmCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["kr-name"]

def code2tpgrphhg(code: str):
    with open(BASE_DIR + "/Data/CodeData/TpgrphHgCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["kr-name"]

def code2roadside(code: str):
    with open(BASE_DIR + "/Data/CodeData/RoadSideCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["kr-name"]


def code2placename(code: str):
    with open(BASE_DIR + "/Data/CodeData/PlaceCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code):
            return d["kr-name"]
        
def code2useplan(code: str):
    with open(BASE_DIR + "/Data/CodeData/LandUsePlanCode.csv") as data:
        csv_mapping = list(csv.DictReader(data))
    for d in csv_mapping:
        if (d["code"] == code[0:6]):
            if code[7] == "1":
                return d["kr-name"] + "<포함>"
            if code[7] == "2":
                return d["kr-name"] + "<저촉>"
            if code[7] == "3":
                return d["kr-name"] + "<접함>"

