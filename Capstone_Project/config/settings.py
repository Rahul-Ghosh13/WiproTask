import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://automationexercise.com")
    timeout: int = int(os.getenv("API_TIMEOUT", "20"))
    test_email: str = os.getenv("TEST_EMAIL", "api.automation@example.com")
    test_password: str = os.getenv("TEST_PASSWORD", "Automation@123")
    test_name: str = os.getenv("TEST_NAME", "API Automation User")


settings = Settings()
