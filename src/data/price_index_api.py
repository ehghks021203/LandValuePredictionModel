import requests

class ProducerPriceIndexAPI():
    url = "https://ecos.bok.or.kr/api/StatisticSearch"
    def __init__(self, key: str) -> None:
        self.url += f"/{key}/json/kr/1/100/404Y014/M"

    def get_data(self, year: int, month: int):
        response = requests.get(f"{self.url}/{year:04d}{month:02d}/{year:04d}{month:02d}/*AA/?/?/?").json()
        if "StatisticSearch" in response:
            return float(response["StatisticSearch"]["row"][0]["DATA_VALUE"])
        else:
            return None

class ConsumerPriceIndexAPI():
    url = "https://ecos.bok.or.kr/api/StatisticSearch"
    def __init__(self, key: str) -> None:
        self.url += f"/{key}/json/kr/1/100/901Y009/M"

    def get_data(self, year: int, month: int):
        response = requests.get(f"{self.url}/{year:04d}{month:02d}/{year:04d}{month:02d}/0/?/?/?").json()
        if "StatisticSearch" in response:
            return float(response["StatisticSearch"]["row"][0]["DATA_VALUE"])
        else:
            return None
        