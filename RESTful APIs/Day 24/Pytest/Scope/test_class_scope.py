import pytest

# Fixture is created once for the class, and reused for all its methods
@pytest.fixture(scope="class")
def class_data():
    print("\n[SETUP] class-level data")
    yield {"name": "pytest"}
    print("\n[TEARDOWN] class-level data")
    
class TestClassScope:
    def test_name(self, class_data):
        print("This is test_name")
        assert class_data["name"] == "pytest"
        
    def test_uppercase(self, class_data):
        print("This is test_uppercase")
        assert class_data["name"].upper() == "PYTEST"
        