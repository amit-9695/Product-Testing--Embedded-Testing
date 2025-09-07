import pytest
from apiex import client

def test_get_posts():
    response=client.get_posts()
    print(f"Response Status Code: {response.status_code}")
    assert response.status_code == 200
    