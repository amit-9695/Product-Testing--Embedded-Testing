# Fixtures can deppend on other fixtures, creating a chain of setup logic.
import pytest

@pytest.fixture
def database():
    print("Setting up database connection")
    return "my_database"

@pytest.fixture
def user(database):
    print(f"creating user with database {database}")
    return f"user_object_using_{database}"

def test_user(user):
    print(f"Running test case with :  {user}")
    assert "user_object_using" in user