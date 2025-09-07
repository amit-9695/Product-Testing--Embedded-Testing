import pytest

@pytest.fixture
def user_data():
    return {"username": "test_user"}

@pytest.fixture
def logged_in_user(user_data):
    user_data["logged_in"] = True
    return user_data

def test_logged_in_user(logged_in_user):
    assert logged_in_user["logged_in"]
    assert logged_in_user["username"] == "test_user"
