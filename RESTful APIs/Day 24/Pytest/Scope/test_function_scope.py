# Function scope(Default scope)- Fixture is created and tear down for each test function
import pytest

@pytest.fixture
def sample_data():
    print("\n[SETUP] Creating sample data")
    yield [1, 2, 3]
    print("\n[TEARDOWN] Cleaning up sample data")
    
def test_sum(sample_data):
    print(f"sum= {sum(sample_data)}")
    assert sum(sample_data) == 6
    
def test_length(sample_data):
    print(f"length= {len(sample_data)}")
    assert len(sample_data) == 3