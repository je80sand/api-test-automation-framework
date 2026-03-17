import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "test_run.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def log_request(method, url, headers=None, body=None):
    logging.info(f"REQUEST: {method} {url}")
    if headers:
        logging.info(f"Headers: {headers}")
    if body:
        logging.info(f"Body: {body}")


def log_response(response):
    logging.info(f"RESPONSE STATUS: {response.status_code}")
    try:
        logging.info(f"RESPONSE BODY: {response.json()}")
    except Exception:
        logging.info(f"RESPONSE TEXT: {response.text}")