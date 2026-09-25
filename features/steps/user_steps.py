import json

from behave import given, then, when

from src.api.payloads import account_payload
from src.api.responses import response_code


def response_body(response):
    try:
        return response.json()
    except (ValueError, json.JSONDecodeError):
        return {}


def register_user(context):
    context.payload = account_payload(context.email, context.password)
    context.response = context.client.create_account(context.payload)
    if response_code(context.response) == 201:
        context.user_created = True


@given("a new API user payload")
def step_new_user_payload(context):
    context.payload = account_payload(context.email, context.password)


@given("a registered API user")
def step_registered_user(context):
    register_user(context)
    assert response_code(context.response) == 201, context.response.text


@when("I create the API user")
def step_create_user(context):
    context.response = context.client.create_account(context.payload)
    if response_code(context.response) == 201:
        context.user_created = True


@when("I retrieve the user by email")
def step_retrieve_user(context):
    context.response = context.client.get_user_detail(context.email)


@when('I update the API user name to "Updated API User"')
def step_update_user(context):
    context.payload["name"] = "Updated API User"
    context.response = context.client.update_account(context.payload)


@when("I verify login with the registered credentials")
def step_verify_login(context):
    context.response = context.client.verify_login(context.email, context.password)


@when("I delete the API user")
def step_delete_user(context):
    context.response = context.client.delete_account(context.email, context.password)
    if response_code(context.response) == 200:
        context.user_created = False


@then("the client should be authenticated")
def step_client_authenticated(context):
    assert context.client.authenticated is True


@then("the response status should be {expected_status:d}")
def step_response_status(context, expected_status):
    assert response_code(context.response) == expected_status, context.response.text


@then('the API response message should be "{expected_message}"')
def step_response_message(context, expected_message):
    assert response_body(context.response).get("message") == expected_message


@then("the returned user email should match the request email")
def step_returned_email(context):
    assert response_body(context.response).get("user", {}).get("email") == context.email
