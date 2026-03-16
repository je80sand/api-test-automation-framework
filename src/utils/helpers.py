from typing import Any


def build_url(base_url: str, endpoint: str) -> str:
    return f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"


def pretty_print_response(response: Any) -> str:
    try:
        return (
            f"STATUS: {response.status_code}\n"
            f"URL: {response.url}\n"
            f"BODY: {response.json()}"
        )
    except Exception:
        return (
            f"STATUS: {response.status_code}\n"
            f"URL: {response.url}\n"
            f"BODY: {response.text}"
        )