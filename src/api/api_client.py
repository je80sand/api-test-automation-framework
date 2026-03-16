import requests

from config.settings import BASE_URL, DEFAULT_HEADERS, TIMEOUT
from src.utils.logger import get_logger


logger = get_logger(__name__)


class APIClient:
    def get(self, endpoint, params=None):
        url = f"{BASE_URL}{endpoint}"
        logger.info(f"GET {url}")
        response = requests.get(
            url,
            params=params,
            headers=DEFAULT_HEADERS,
            timeout=TIMEOUT,
        )
        logger.info(f"Status Code: {response.status_code}")
        return response

    def post(self, endpoint, data=None):
        url = f"{BASE_URL}{endpoint}"
        logger.info(f"POST {url}")
        response = requests.post(
            url,
            json=data,
            headers=DEFAULT_HEADERS,
            timeout=TIMEOUT,
        )
        logger.info(f"Status Code: {response.status_code}")
        return response

    def put(self, endpoint, data=None):
        url = f"{BASE_URL}{endpoint}"
        logger.info(f"PUT {url}")
        response = requests.put(
            url,
            json=data,
            headers=DEFAULT_HEADERS,
            timeout=TIMEOUT,
        )
        logger.info(f"Status Code: {response.status_code}")
        return response

    def delete(self, endpoint):
        url = f"{BASE_URL}{endpoint}"
        logger.info(f"DELETE {url}")
        response = requests.delete(
            url,
            headers=DEFAULT_HEADERS,
            timeout=TIMEOUT,
        )
        logger.info(f"Status Code: {response.status_code}")
        return response