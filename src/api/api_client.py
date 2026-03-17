import requests

from config import settings
from src.utils.logger import log_request, log_response


class APIClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.timeout = settings.TIMEOUT
        self.headers = settings.DEFAULT_HEADERS

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        log_request("GET", url, headers=self.headers, body=params)

        response = requests.get(
            url,
            params=params,
            headers=self.headers,
            timeout=self.timeout,
        )

        log_response(response)
        return response

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        log_request("POST", url, headers=self.headers, body=data)

        response = requests.post(
            url,
            json=data,
            headers=self.headers,
            timeout=self.timeout,
        )

        log_response(response)
        return response

    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        log_request("PUT", url, headers=self.headers, body=data)

        response = requests.put(
            url,
            json=data,
            headers=self.headers,
            timeout=self.timeout,
        )

        log_response(response)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        log_request("DELETE", url, headers=self.headers)

        response = requests.delete(
            url,
            headers=self.headers,
            timeout=self.timeout,
        )

        log_response(response)
        return response