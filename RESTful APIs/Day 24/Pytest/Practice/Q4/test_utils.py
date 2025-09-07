import requests
from utils import get_user

def test_get_user_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Leanne Graham"}
    mocker.patch("requests.get", return_value=mock_response)
    user = get_user(1)
    assert user["name"] == "Leanne Graham"
def test_get_user_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch("requests.get", return_value=mock_response)

    user = get_user(999)
    assert user is None

