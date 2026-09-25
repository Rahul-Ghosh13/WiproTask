from typing import Any


def account_payload(email: str, password: str, name: str = "API Automation User") -> dict[str, Any]:
    return {
        "name": name,
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "15",
        "birth_month": "6",
        "birth_year": "1990",
        "firstname": "API",
        "lastname": "Automation",
        "company": "Wipro",
        "address1": "1 Test Street",
        "address2": "Test District",
        "country": "India",
        "zipcode": "560001",
        "state": "Karnataka",
        "city": "Bengaluru",
        "mobile_number": "9999999999",
    }
