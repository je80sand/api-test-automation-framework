import requests

from config import settings
from src.utils.logger import get_logger


logger = get_logger(__name__)


class APIClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.timeout = settings.TIMEOUT
        self.headers = settings.DEFAULT_HEADERS

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = requests.get(
            url,
            params=params,
            headers=self.headers,
            timeout=self.timeout,
        )
        logger.info(f"Status Code: {response.status_code}")
        return response

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        response = requests.post(
            url,
            json=data,
            headers=self.headers,
            timeout=self.timeout,
        )
        logger.info(f"Status Code: {response.status_code}")
        return response

    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        response = requests.put(
            url,
            json=data,
            headers=self.headers,
            timeout=self.timeout,
        )
        logger.info(f"Status Code: {response.status_code}")
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = requests.delete(
            url,
            headers=self.headers,
            timeout=self.timeout,
        )
        logger.info(f"Status Code: {response.status_code}")
        return response