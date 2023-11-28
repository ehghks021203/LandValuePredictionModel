from mykey import KAKAO_API_KEY, VWORLD_API_KEY
from PyKakao import Local
from enum import Enum
import json
import requests
import math
import csv
import pandas as pd
import numpy as np

CSV_DIR_PATH = "/home/students/cs/202120990/LandValuePredictionModel/data/"

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
    local = Local(service_key=KAKAO_API_KEY)
    sa = local.search_address(address)
    if (len(sa["documents"]) == 0):
        return None
    for c in Category.list():
        distance =  local.search_category(c, x=sa["documents"][0]["x"], y=sa["documents"][0]["y"], radius=20000, sort="distance")
        rd[c] = int(distance["documents"][0]["distance"])
    return rd

def get_place_count_in_radius(address: str, radius: 25):
    rd = {}
    local = Local(service_key=KAKAO_API_KEY)
    sa = local.search_address(address)
    for c in Category.list():
        distance =  local.search_category(c, x=sa["documents"][0]["x"], y=sa["documents"][0]["y"], radius=radius)
        rd["{}_{}m".format(c, radius)] = int(distance["meta"]["total_count"])
    return rd

def get_place_count_in_radius_with_vworld(address: str):
    # 로컬 API 인스턴스 생성
    local = Local(service_key=KAKAO_API_KEY)
    sa = local.search_address(address)
    
    lat = float(sa["documents"][0]["y"])
    lng = float(sa["documents"][0]["x"])
    x = (lng * 20037508.34) / 180;
    y = math.log(math.tan(((90 + lat) * math.pi) / 360)) / (math.pi / 180);
    y = (y * 20037508.34) / 180;

    # 엔드포인트
    endpoint = "http://api.vworld.kr/req/data"

    # 요청 파라미터
    service = "data"
    key = VWORLD_API_KEY
    request = "GetFeature"
    data = "LT_C_DHSCH"
    page = 1
    size = 1000
    crs = "EPSG:4326"
    buffer = 10000
    geomfilter = f"POINT({x} {y})"

    # 요청 URL
    url = f"{endpoint}?service={service}&request={request}&data={data}&key={key}&page={page}&size={size}&attribute=true&crs={crs}&buffer={buffer}&geomfilter={geomfilter}"
    print(url)
    # 요청 결과
    res = json.loads(requests.get(url).text)
    print(res)
    """ TODO: VWorld를 이용해 주변 상권 개수 받아오기
    
        Kakao Local API는 데이터 기준일자가 나와있지 않기 때문에 년도별 상권 변화를 감지하기 어려움.
        따라서 Kakao Local API를 사용하여 데이터셋에 넣기에는 무리가 있어보임.
        => VWorld를 이용해 데이터 추출 시도
    """

if __name__ == "__main__":
    df = pd.read_csv(CSV_DIR_PATH + "seoul_data_origin.csv")
    columns = Category.list() + Category.list(prefix="_500m") + Category.list(prefix="_1000m") + Category.list(prefix="_3000m")
    place_mat = np.empty((len(df), len(columns)))
    place_mat[:] = np.nan
    place_df = pd.DataFrame(place_mat, columns=columns)

    LIM = 3000
    passed = 0
    for i in range(len(df)):
        if i > LIM + passed:
            break
        addr = df.iloc[i]["LdCodeNm"] + " "
        addr += df.iloc[i]["RegstrSeCodeNm"] if df.iloc[i]["RegstrSeCodeNm"] == "산" else ""
        addr += str(int(str(df.iloc[i]["PNU"])[11:15])) + "-" + str(int(str(df.iloc[i]["PNU"])[15:19]))
        print("{:30s} | {:3d}/{:3d} ({:5.2f}%)".format(addr, i-passed, LIM, (i-passed)/LIM * 100), end="")
        rd = get_nearest_place_distance(addr)
        if rd == None:
            print("\n\t====== PASSED ======")
            passed += 1
            continue
        rd.update(get_place_count_in_radius(addr, 500))
        rd.update(get_place_count_in_radius(addr, 1000))
        rd.update(get_place_count_in_radius(addr, 3000))
        
        for k, v in rd.items():
            place_df.loc[i, k] = v
        print("\r{:30s} | {:3d}/{:3d} ({:5.2f}%)".format(addr, i-passed+1, LIM, (i-passed+1)/LIM * 100))
    df = df.join(place_df.add_prefix("LandPlace_"))
    df = df.dropna()
    df = df.reset_index(drop=True)
    #df.drop([""], axis=1, inplace=True)
    df.to_csv(CSV_DIR_PATH + f"seoul_data_add_place_{LIM}.csv", index=None)