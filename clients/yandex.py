from clients import Clients


class YandexClient(Clients):
    text = ""
    __api_key: str = "dict.1.1.20221101T151346Z.8cc25df7c1c42d3f.336df7ad85bdc19d9c7897abdc882a41a135d01b"
    __url: str = f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={__api_key}&lang=en-ru&text="
