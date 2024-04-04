import crawling_land_price_data as clpd
import get_land_feature_data as glfd
import get_fluctuation_rate_of_land_price as gfrolp
import get_price_index_data as gpid
import get_land_use_plan_data as glupd
import get_place_data as gpd
import convert_code as cc
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from config import BASE_DIR

SAVE_FILE_NAME = "Dataset.csv"
IS_INCLUDE_PLACE_DATA = True

if __name__ == "__main__":
    lat, lng = clpd.get_break_point()
    count = 0
    actual = 0

    while True:
        land_list = clpd.get_crawling_data(lat,lng)
        land_dict = {}

        for land in land_list:
            if int(land["Year"]) > 2012:
                land["Price"] = int(land["Price"]*10000/land["DealArea"])

                # Get land feature data
                result = glfd.get_data(land["PNU"], land["Year"])
                if result == None:
                    break
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
                result = gfrolp.get_by_region(land["PNU"][0:10], int(land["Year"]), int(land["Month"]))
                land["PclndIndex"] = result["pclndIndex"]
                land["PclndChgRt"] = result["pclndChgRt"]
                land["AcmtlPclndChgRt"] = result["acmtlPclndChgRt"]

                result = gfrolp.get_large_cl_by_region(land["PNU"][0:10], int(land["Year"]), int(land["Month"]))
                land["LargeClPclndIndex"] = result["pclndIndex"]
                land["LargeClPclndChgRt"] = result["pclndChgRt"]
                land["LargeClAcmtlPclndChgRt"] = result["acmtlPclndChgRt"]


                # if cc.code2zoning(land["PrposArea1"][2:]) == "":
                #     land["PclndIndexByZoning"] = None
                #     land["PclndChgRtByZoning"] = None
                #     land["AcmtlPclndChgRtByZoning"] = None
                # else:
                #     result = gfrolp.get_by_zoning(land["PNU"][0:10], int(land["Year"]), int(land["Month"]))
                #     print(land["PrposArea1"][2:])
                #     land["PclndIndexByZoning"] = result[cc.code2zoning(land["PrposArea1"][2:]) + "Index"]
                #     land["PclndChgRtByZoning"] = result[cc.code2zoning(land["PrposArea1"][2:]) + "ChgRt"]
                #     land["AcmtlPclndChgRtByZoning"] = result[cc.code2zoning(land["PrposArea1"][2:]) + "Acmtl"]

                # Get fluctuation rate of land price data
                # result = gfrolp.get_by_land_category(land["PNU"][0:10], int(land["Year"]), int(land["Month"]))
                # land["PclndIndexByLandCategory"] = result[cc.code2landcategory(land["LadUseSittn"][2:]) + "Index"]
                # land["PclndChgRtByLandCategory"] = result[cc.code2landcategory(land["LadUseSittn"][2:]) + "ChgRt"]
                # land["AcmtlPclndChgRtByLandCategory"] = result[cc.code2landcategory(land["LadUseSittn"][2:]) + "Acmtl"]
                
                # Get price index data
                result = gpid.get_producer_price_index_data(int(land["Year"]), int(land["Month"]))
                if result == None:
                    break
                land["PPI"] = result
                result = gpid.get_consumer_price_index_data(int(land["Year"]), int(land["Month"]))
                if result == None:
                    break
                land["CPI"] = result

                if IS_INCLUDE_PLACE_DATA:
                    rd = gpd.get_nearest_place_distance(addr)
                    rd_500 = gpd.get_place_count_in_radius(addr, 500)
                    rd_1000 = gpd.get_place_count_in_radius(addr, 1000)
                    rd_3000 = gpd.get_place_count_in_radius(addr, 3000)
                    if rd == None or rd_500 == None or rd_1000 == None or rd_3000 == None:
                        break

                    for category in gpd.Category.list():
                        land[category] = rd[category]
                        land[category + "_500m"] = rd_500[category]
                        land[category + "_1000m"] = rd_1000[category]
                        land[category + "_3000m"] = rd_3000[category]


                result = glupd.get_data(land["PNU"])
                if result == None:
                    break
                land["LandUsePlans"] = result
                land_dict = land
                actual += 1
                clpd.save_crawling_data(land_dict, SAVE_FILE_NAME)
                break
        print("\r{:3.10f},{:3.10f} | {:4d} ({} loss)".format(lat, lng, count, count - actual), end="")
        lat, lng = clpd.next_step(lat, lng)
        clpd.save_break_point(lat, lng)
        count += 1
