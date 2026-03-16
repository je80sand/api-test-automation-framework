import allure
import pytest

from src.api.endpoints import USERS


@allure.feature("Health Check")
@allure.story("API availability")
@pytest.mark.api
@pytest.mark.smoke
def test_api_health_check(api_client):
    response = api_client.get(USERS)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 5