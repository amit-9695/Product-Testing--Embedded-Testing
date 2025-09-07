# Using fixture for setup and teardown
# Fixture can include setup and teardown logic using yield
import pytest

@pytest.fixture
def resource_setup_teardown():
    print("setting up resource")
    resource = {"status": "ready"}
    yield resource  # This is where the test will run
    print("tearing down resource")
    
def test_resource_usage(resource_setup_teardown):
    assert resource_setup_teardown["status"] == "ready"