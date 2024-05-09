import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from land_api import LandFeatureAPI, LandUsePlanAPI, FluctuationRateOfLandPriceAPI
from price_index_api import ProducerPriceIndexAPI, ConsumerPriceIndexAPI
import get_place_data as gpd

from config import Dataset, API

def make(pnu: str, date: str):
    land = {
        "PNU": pnu,
        "Year": int(date[0:4]),
        "Month": int(date[4:6])
    }

    # Get land feature data
    lf_api = LandFeatureAPI(API.LAND_API_KEY)
    result = lf_api.get_data(land["PNU"], land["Year"])
    if result == None:
        sys.exit("Failed to fetch land characteristic data from the API.")

    addr = result["ldCodeNm"] + " "
    addr += result["regstrSeCodeNm"] if result["regstrSeCodeNm"] == "산" else ""
    addr += str(int(str(land["PNU"])[11:15])) + "-" + str(int(str(land["PNU"])[15:19]))
    land["PblntfPclnd"] = result["pblntfPclnd"]
    land["RegstrSe"] = "Re" + result["regstrSeCode"]
    land["Lndcgr"] = "Lc" + result["lndcgrCode"]
    land["LndpclAr"] = result["lndpclAr"]
    land["PrposArea1"] = "A1" + result["prposArea1"]
    land["PrposArea2"] = "A2" + result["prposArea2"]
    land["LadUseSittn"] = "Us" + result["ladUseSittn"]
    land["TpgrphHg"] = "Hg" + result["tpgrphHgCode"]
    land["TpgrphFrm"] = "Fm" + result["tpgrphFrmCode"]
    land["RoadSide"] = "Rs" + result["roadSideCode"]
    
    # Get fluctuation rate of land price data
    frolp_api = FluctuationRateOfLandPriceAPI(API.LAND_API_KEY)
    result = frolp_api.get_data_by_region(land["PNU"][0:10], int(land["Year"]), int(land["Month"]))
    land["PclndIndex"] = result["pclndIndex"]
    land["PclndChgRt"] = result["pclndChgRt"]
    land["AcmtlPclndChgRt"] = result["acmtlPclndChgRt"]

    result = frolp_api.get_data_by_large_region(land["PNU"][0:10], int(land["Year"]), int(land["Month"]))
    land["LargeClPclndIndex"] = result["pclndIndex"]
    land["LargeClPclndChgRt"] = result["pclndChgRt"]
    land["LargeClAcmtlPclndChgRt"] = result["acmtlPclndChgRt"]

    # Get price index data
    ppi_api = ProducerPriceIndexAPI(API.ECOS_KEY)
    result = ppi_api.get_data(int(land["Year"]), int(land["Month"]))
    print(ppi_api.url)
    if result == None:
        sys.exit("Failed to fetch producer price index data from the API.")
    land["PPI"] = result
    cpi_api = ConsumerPriceIndexAPI(API.ECOS_KEY)
    result = cpi_api.get_data(int(land["Year"]), int(land["Month"]))
    if result == None:
        sys.exit("Failed to fetch customer price index data from the API.")
    land["CPI"] = result

    if Dataset.IS_INCLUDE_PLACE_DATA:
        rd = gpd.get_nearest_place_distance(addr)
        rd_500 = gpd.get_place_count_in_radius(addr, 500)
        rd_1000 = gpd.get_place_count_in_radius(addr, 1000)
        rd_3000 = gpd.get_place_count_in_radius(addr, 3000)
        if rd == None or rd_500 == None or rd_1000 == None or rd_3000 == None:
            sys.exit("Failed to fetch place data from the API.")

        for category in gpd.Category.list():
            land[category] = rd[category]
            land[category + "_500m"] = rd_500[category]
            land[category + "_1000m"] = rd_1000[category]
            land[category + "_3000m"] = rd_3000[category]


    lup_api = LandUsePlanAPI(API.LAND_API_KEY)
    result = lup_api.get_data(land["PNU"])
    if result == None:
        sys.exit("Failed to fetch land use plans data from the API.")
    land["LandUsePlans"] = result

    return land

if __name__ == "__main__":
    target_pnu = "1147010100109370018"
    target_date = "202312"
    target_land = make(target_pnu, target_date)
    print(target_land)