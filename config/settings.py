import os
from pathlib import Path

from dotenv import load_dotenv


def load_environment(env_name: str = "dev") -> None:
    env_file = Path(__file__).resolve().parent / f".env.{env_name}"
    load_dotenv(env_file, override=True)


ENV_NAME = os.getenv("ENV_NAME", "dev")
BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))

DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}