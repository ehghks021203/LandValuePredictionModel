import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from config import BASE_DIR, API

def get_data(pnu: str):
    param = {
        "key": API.LAND_API_KEY,
        "format": "json",
        "numOfRows": "100",
        "pageNo": "1",
        "pnu": pnu
    }
    request_data = requests.get(API.LAND_USE_PLAN_URL, params=param)
    request = request_data.json()
    if "landUses" in request:
        datas = request["landUses"]["field"]
        land_use_plan_list = []
        for d in datas:
            land_use_plan_list.append("{}({})".format(d["prposAreaDstrcCode"], d["cnflcAt"]))
        land_use_plan_list = list(set(land_use_plan_list))
        
        land_use_plan_str = ""
        for l in land_use_plan_list:
            land_use_plan_str += l + "/"
        return land_use_plan_str[:-1]
    else:
        return None