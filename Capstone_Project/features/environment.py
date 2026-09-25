from datetime import datetime, timezone

from src.api.client import ApiClient
from src.api.responses import response_code


def before_all(context):
    context.client = ApiClient()


def before_scenario(context, scenario):
    context.response = None
    context.payload = None
    context.email = f"api.automation.{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}@example.com"
    context.password = "Automation@123"
    context.user_created = False


def after_scenario(context, scenario):
    if context.user_created:
        cleanup = context.client.delete_account(context.email, context.password)
        if response_code(cleanup) not in (200, 404):
            scenario.attach(cleanup.text, "text/plain", "cleanup-response")


def after_all(context):
    context.client.close()
