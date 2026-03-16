import pytest

from config.settings import load_environment
from src.api.api_client import APIClient


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against: dev | stage | prod",
    )


def pytest_configure(config):
    env_name = config.getoption("--env")
    load_environment(env_name)


@pytest.fixture(scope="session")
def api_client():
    return APIClient()