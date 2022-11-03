from clients import Clients


class VKController:
    __protocol: str = "https://"
    __address: str = "api.vk.com/method"
    __method: str = ""
    __params: str = ""
    __access_token: str = ""
    __V: str = "5.131"

    __url: str = ""

    __response = None

    def __make_url(self):
        self.__url = "{0}{1}{2}{3}".format(
            self.__protocol,
            self.__address,
            self.__method,
            self.__params
        )

    def __send_request(self) -> None:
        clients = Clients(
            method="GET",
            url=self.__url
        )

        self.__response = clients.get_response()

    def get_response_data(self):
        self.__send_request()
        if self.__response.status_code != 200:
            raise Exception("Error with status: {0}".format(self.__response.status_code))
        return self.__response.json()

    def get_users(self, user_id: str):
        self.__method = "/users.get"
        self.__params = "?user_id="+user_id
        self.__make_url()

        self.__response = self.get_response_data()
        # print(self.__response)
        return self.__response

    def oauth_authorize(self):
        url: str = "https://oauth.vk.com/authorize"
        client_id: str = ""
        redirect_uri: str = ""
        display: str = ""
        scope: str = ""
        response_type: str = ""
        state: str = ""

        self.get_response_data()
