import requests
import xmltodict

class LandFeatureAPI():
    url = "https://api.vworld.kr/ned/data/getLandCharacteristics"
    def __init__(self, key: str) -> None:
        self.default_params = {
            "key": key,
            "format": "json",
            "numOfRows": "100",
            "pageNo": "1"
        }
    
    def get_data(self, pnu: str, year: int, assorted=False):
        params = {"pnu":pnu,"stdrYear":year}
        params.update(self.default_params)
        response = requests.get(self.url, params=params).json()
        if "landCharacteristicss" in response:
            if assorted:
                return response["landCharacteristicss"]["field"]
            else:
                return response["landCharacteristicss"]["field"][0]
        else:
            return None

class LandTradeAPI():
    url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcLandTrade"
    def __init__(self, key: str) -> None:
        self.default_params = {
            "serviceKey": key,
            "numOfRows": "100",
            "pageNo": "1"
        }
    
    def get_data(self, pnu: str, year: int, month: int):
        params = {"LAWD_CD":pnu,"DEAL_YMD":f"{year:04d}{month:02d}"}
        params.update(self.default_params)
        response = xmltodict.parse(requests.get(self.url, params=params).text)
        if response["response"]["header"]["resultCode"] == "00":
            if response["response"]["body"]["totalCount"] == "0":
                return None
            else:
                return response["response"]["body"]["items"]["item"]
        
class LandUsePlanAPI():
    url = "https://api.vworld.kr/ned/data/getLandUseAttr"
    def __init__(self, key: str) -> None:
        self.default_params = {
            "key": key,
            "format": "json",
            "numOfRows": "100",
            "pageNo": "1"
        }
    
    def get_data(self, pnu: str):
        params = {"pnu":pnu}
        params.update(self.default_params)
        response = requests.get(self.url, params=params).json()
        if "landUses" in response:
            datas = response["landUses"]["field"]
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
            
        
class FluctuationRateOfLandPriceAPI():
    by_region_url = "https://api.vworld.kr/ned/data/getByRegion"
    by_large_region_url = "https://api.vworld.kr/ned/data/getLargeCLByRegion"
    def __init__(self, key: str) -> None:
        self.default_params = {
            "key": key,
            "format": "json",
            "numOfRows": "100",
            "pageNo": "1",
            "scopeDiv": "A"
        }
    
    def get_data_by_region(self, ld_code: str, year: int, month: int):
        params = {"reqLdCode":ld_code,"stdrYear":year, "stdrMt": f"{month:02d}"}
        params.update(self.default_params)
        response = requests.get(self.by_region_url, params=params).json()
        if "byRegions" in response:
            return response["byRegions"]["field"][0]
        else:
            return None            
    
    def get_data_by_large_region(self, ld_code: str, year: int, month: int):
        params = {"stdrYear":year, "stdrMt": f"{month:02d}"}
        params.update(self.default_params)
        response = requests.get(self.by_large_region_url, params=params).json()
        for data in response["byRegions"]["field"]:
            if data["ldCtprvnCode"] == ld_code[0:2]:
                return data
        return None
