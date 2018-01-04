import os

import requests

from api_methods import ApiMethods
from response import Response

class Client(ApiMethods):
    def __init__(self, access_token, current_team):
        self.access_token = access_token
        self.current_team = current_team
        self.api_endpoint = self.__api_endpoint()

    def send_get(self, path, params=None, headers=None):
        return self.send_request("get", path, params, headers)

    def __api_endpoint(self):
        return os.environ.get("ESA_API_ENDPOINT", "https://api.esa.io")

    def send_request(self, http_method, path, params=None, headers=None):
        url = "{endpoint}/{path}?access_token={access_token}".format(endpoint=self.api_endpoint,
                                                                     path=path,
                                                                     access_token=self.access_token)

        response = requests.__getattribute__(http_method)(url, params=params, headers=headers)

        return Response(response)
