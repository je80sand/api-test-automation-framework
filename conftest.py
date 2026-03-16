import pytest

from src.api.api_client import APIClient


@pytest.fixture(scope="session")
def api_client() -> APIClient:
    return APIClient()