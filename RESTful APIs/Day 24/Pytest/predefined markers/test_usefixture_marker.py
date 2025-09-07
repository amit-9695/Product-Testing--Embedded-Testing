# usefixtures marker - apply a fixture to a test function or class
import pytest

@pytest.fixture
def setup_data():
    return {"key1": "value1"}

@pytest.mark.usefixtures("setup_data")
def test_usefixture(setup_data):
    # The fixture setup_data is applied to this test
    assert setup_data["key1"] == "value1"