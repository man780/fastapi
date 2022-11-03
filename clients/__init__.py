import requests


class Clients:
    __url: str = None
    __method: str = "GET"
    __headers: dict = None
    __params: dict = None
    __data: str = None
    __response = None

    @classmethod
    def __validate_is_none(cls, arg) -> bool:
        if arg:
            return True
        return False

    def __init__(
            self,
            url: str,
            method: str,
            data: str = None,
            headers: dict = None,
            params: dict = None
    ) -> None:
        if self.__validate_is_none(url):
            self.__url = url
        if self.__validate_is_none(method):
            self.__method = method
        self.__headers = headers
        self.__data = data
        self.__params = params

    def __send_request(self) -> None:
        try:
            self.__response = requests.request(
                method=self.__method,
                url=self.__url,
                data=self.__data,
                headers=self.__headers,
                params=self.__params
            )
        except Exception as exp:
            raise f"Error on request {str(exp)}"

    def get_response_data(self) -> dict:
        self.__send_request()
        response = self.__response.json()
        return response

    def get_response(self):
        self.__send_request()
        return self.__response
