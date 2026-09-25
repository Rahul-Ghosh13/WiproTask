from typing import Any

import requests

from config.settings import settings


class ApiClient:

    def __init__(self, base_url: str = settings.base_url, timeout: int = settings.timeout):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
        self.authenticated = False

    def request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        """Send a request and keep the raw response available for assertions."""
        url = f"{self.base_url}/{path.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)
        return self.session.request(method=method, url=url, **kwargs)

    def verify_login(self, email: str, password: str) -> requests.Response:
        response = self.request(
            "POST",
            "/api/verifyLogin",
            data={"email": email, "password": password},
        )
        self.authenticated = response.status_code == 200
        return response

    def create_account(self, account: dict[str, Any]) -> requests.Response:
        return self.request("POST", "/api/createAccount", data=account)

    def get_user_detail(self, email: str) -> requests.Response:
        return self.request("GET", "/api/getUserDetailByEmail", params={"email": email})

    def update_account(self, account: dict[str, Any]) -> requests.Response:
        return self.request("PUT", "/api/updateAccount", data=account)

    def delete_account(self, email: str, password: str) -> requests.Response:
        return self.request(
            "DELETE",
            "/api/deleteAccount",
            data={"email": email, "password": password},
        )

    def close(self) -> None:
        self.session.close()
