import pytest

@pytest.fixture(autouse=True)

def auto_setup_teardown():
    print("[SETUP] runs before each test")
    yield
    print("[TEARDOWN] runs after each test")
    
def test_one():
    print("Running test_one")
    assert 1+1 == 2
    
def test_two():
    print("Running test_two")
    assert 2*2 == 4