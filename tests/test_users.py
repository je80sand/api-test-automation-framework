import allure
import pytest

from data.users_payloads import CREATE_USER_PAYLOAD, UPDATE_USER_PAYLOAD
from src.api.endpoints import USERS, SINGLE_USER


@allure.feature("Users")
@pytest.mark.api
def test_get_users_list(api_client):
    response = api_client.get(USERS)

    assert response.status_code == 200
    users = response.json()

    assert isinstance(users, list)
    assert len(users) > 0


@allure.feature("Users")
@pytest.mark.api
def test_get_single_user(api_client):
    response = api_client.get(SINGLE_USER.format(user_id=1))

    assert response.status_code == 200
    user = response.json()

    assert user["id"] == 1


@allure.feature("Users")
@pytest.mark.api
def test_create_user(api_client):
    response = api_client.post(USERS, CREATE_USER_PAYLOAD)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == CREATE_USER_PAYLOAD["name"]
    assert data["job"] == CREATE_USER_PAYLOAD["job"]


@allure.feature("Users")
@pytest.mark.api
def test_update_user(api_client):
    response = api_client.put(
        SINGLE_USER.format(user_id=1),
        UPDATE_USER_PAYLOAD
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == UPDATE_USER_PAYLOAD["name"]


@allure.feature("Users")
@pytest.mark.api
def test_delete_user(api_client):
    response = api_client.delete(SINGLE_USER.format(user_id=1))

    assert response.status_code == 200