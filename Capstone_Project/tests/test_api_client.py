import responses

from src.api.client import ApiClient


@responses.activate
def test_verify_login_updates_authentication_state():
    responses.add(
        responses.POST,
        "https://automationexercise.com/api/verifyLogin",
        json={"responseCode": 200, "message": "User exists!"},
        status=200,
    )

    client = ApiClient()
    response = client.verify_login("user@example.com", "secret")

    assert response.status_code == 200
    assert client.authenticated is True
    assert responses.calls[0].request.body == "email=user%40example.com&password=secret"


@responses.activate
def test_get_user_detail_uses_email_query_parameter():
    responses.add(
        responses.GET,
        "https://automationexercise.com/api/getUserDetailByEmail",
        json={"responseCode": 200, "user": {"email": "user@example.com"}},
        status=200,
    )

    response = ApiClient().get_user_detail("user@example.com")

    assert response.status_code == 200
    assert responses.calls[0].request.url.endswith("?email=user%40example.com")
