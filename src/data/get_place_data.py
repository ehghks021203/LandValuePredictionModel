from PyKakao import Local
from enum import Enum
from config import API

class Category(Enum):
    MT = "MT1"  # 대형마트
    CS = "CS2"  # 편의점
    PS = "PS3"  # 어린이집, 유치원
    SC = "SC4"  # 학교
    AC = "AC5"  # 학원
    PK = "PK6"  # 주차장
    OL = "OL7"  # 주유소, 충전소
    SW = "SW8"  # 지하철역
    BK = "BK9"  # 은행
    CT = "CT1"  # 문화시설
    AG = "AG2"  # 중개업소
    PO = "PO3"  # 공공기관
    AT = "AT4"  # 관광명소
    AD = "AD5"  # 숙박
    FD = "FD6"  # 음식점
    CE = "CE7"  # 카페
    HP = "HP8"  # 병원
    PM = "PM9"  # 약국

    @classmethod
    def list(cls, prefix=""):
        return [c.value + prefix for c in cls]

def get_nearest_place_distance(address: str):
    rd = {}
    local = Local(service_key=API.KAKAO_API_KEY)
    sa = local.search_address(address)
    if (len(sa["documents"]) == 0):
        return None
    for c in Category.list():
        distance =  local.search_category(c, x=sa["documents"][0]["x"], y=sa["documents"][0]["y"], radius=20000, sort="distance")
        if len(distance["documents"]) == 0:
            rd[c] = 20000
        else:
            rd[c] = int(distance["documents"][0]["distance"])
    return rd

def get_place_count_in_radius(address: str, radius: 25):
    rd = {}
    local = Local(service_key=API.KAKAO_API_KEY)
    sa = local.search_address(address)
    if len(sa["documents"]) == 0:
        return None
    for c in Category.list():
        distance =  local.search_category(c, x=sa["documents"][0]["x"], y=sa["documents"][0]["y"], radius=radius)
        rd[c] = int(distance["meta"]["total_count"])
    return rd

