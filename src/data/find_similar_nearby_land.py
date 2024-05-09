import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('')))
import convert_code as cc
import make_input_data as mid
from land_api import LandTradeAPI, LandFeatureAPI
from config import API

def _decrement_month(year: int, month: int) -> tuple:
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    return year, month

def _get_nearby_land_trade_data(pnu: str, year: int, month: int, land: dict) -> dict:
    api = LandTradeAPI(API.LAND_TRADE_API_KEY)
    compare_land_trade = {}
    target_year = year
    target_month = month
    
    # Exception
    if not "Lndcgr" in land or not "PrposArea1" in land:
        sys.exit("The 'land' parameter must contain the key values 'Lndcgr' and 'PrposArea1'.")
    
    eupmyeondong = cc.code2addr(pnu).split(" ")[2]
    print(eupmyeondong)
    
    try:
        while True:
            results = api.get_data(pnu[:5], target_year, target_month)
            if result == None:
                target_year, target_month = _decrement_month(target_year, target_month)
                if target_year < 2015:
                    return None
                continue
            for r in results:
                if isinstance(r, dict):
                    if r["지목"] == cc.code2lndcgr(land["Lndcgr"][2:4]):
                        if r["용도지역"] == cc.code2zoning(land["PrposArea1"][2:4]):
                            return r
            target_year, target_month = _decrement_month(target_year, target_month)
            if target_year < 2015:
                return None
    except Exception as e:
        print("Exception:", e)

def _mapping_pnu_code(land: dict) -> str:
    addr = cc.code2addr(land["지역코드"])
    #if land["지번"][0] == "산":
        
    #elif land["지번"][0] == "*":
        
    #else:
            
def _get_similar_land_feature_data(pnu: str, year: int, land: dict):
    api = LandFeatureAPI(API.LAND_API_KEY)
    results = api.get_data(_mapping_pnu_code(land), year, assorted=True)
            
def get_data(pnu: str, year: int, month: int, land: dict):
    land_trade_data = _get_nearby_land_trade_data(pnu, year, month, land)
    if land_trade_data == None:
        return None
    land_feature_data = _get_similar_land_feature_data(pnu, year, land_trade_data)
    
    
        
if __name__ == "__main__":
    target_pnu = "1147010100109370018"
    target_date = "202312"
    target_land = mid.make(target_pnu, target_date)
    _get_nearby_land_trade_data(target_pnu, 2023, 12, target_land)
    