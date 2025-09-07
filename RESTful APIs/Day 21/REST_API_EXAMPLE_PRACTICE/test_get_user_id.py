import requests
import pytest

BASE_URL = "https://reqres.in/api"

def test_get_single_user():
    user_id= 2
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    response_data = response.json()
    assert "data" in response_data
    response_data["data"]["first_name"] = "Janet"
    print(f"Status Code: {response.status_code}")
    print(f"Responsse bosdy: {response_data}")
    print(f"First Name: {response_data['data']['first_name']}")