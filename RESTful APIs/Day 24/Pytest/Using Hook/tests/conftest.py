import pytest
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

@pytest.fixture
def env(pytestconfig):
    return pytestconfig.getoption("--env")
