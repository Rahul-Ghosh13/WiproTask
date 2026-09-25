from typing import Any

import requests


def response_code(response: requests.Response) -> int:
    """Return the service responseCode, falling back to HTTP status."""
    try:
        body: dict[str, Any] = response.json()
    except ValueError:
        return response.status_code
    return int(body.get("responseCode", response.status_code))
