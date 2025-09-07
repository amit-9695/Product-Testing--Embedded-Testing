import pytest

@pytest.fixture(scope="session")
def database_connection():
    print("\nSetting up database connection")
    conn = {"db": "connected"}
    yield conn
    print("\nTearing down database connection")
