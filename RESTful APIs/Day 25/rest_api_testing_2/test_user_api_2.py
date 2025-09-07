import requests

def test_get_single_user(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2