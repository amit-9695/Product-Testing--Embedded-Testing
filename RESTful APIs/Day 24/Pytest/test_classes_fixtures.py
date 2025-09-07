# Grouping with Test Classes Fixtures
# combine classes and fixtures for better setup and teardown management.
import pytest

@pytest.fixture
def setup_data():
    return {"key1": "value1"}

class TestAPI:
    def test_get_data(self, setup_data):
        assert setup_data["key1"] == "value1"
        
    def test_set_data(self, setup_data):
        setup_data["key2"] = "value2"
        assert "key2" in setup_data