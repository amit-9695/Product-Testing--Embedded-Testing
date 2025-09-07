import requests
import pytest


BASE_URL = "https://reqres.in/api"

# read(GET) - ALL Posts

def test_get_posts():
    response = requests.get(f"{BASE_URL}/users?page=2")


    # Convert response to JSON and print it
    posts = response.json()
    print("Response JSON:", posts)
    print(f"Response Status Code: {response.status_code}")
    assert response.status_code == 200