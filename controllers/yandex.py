from clients import Clients


class YandexController:
    __domain_url: str = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"
    __key: str = "dict.1.1.20221103T162355Z.d1018879e1a8d3ec.2d95e1398f95d571fdd5e9013e1193e27f585bca"
    __response: dict = None
    __url: str = ""

    def configure_url(self, text: str) -> None:
        data = "?key={0}&lang=en-ru&text={1}".format(self.__key, text)
        self.__url = self.__domain_url+data

    def __send_request(self) -> None:
        clients = Clients(
            method="GET",
            url=self.__url
        )

        self.__response = clients.get_response()

    def get_response_data(self):
        self.__send_request()
        # if self.__response.status_code == 403:
        #     raise 403
        if self.__response.status_code != 200:
            raise Exception("Error with status: {0}".format(self.__response.status_code))
        return self.__response.json()
