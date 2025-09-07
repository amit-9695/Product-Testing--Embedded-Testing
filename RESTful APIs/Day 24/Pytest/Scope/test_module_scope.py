import pytest

@pytest.fixture(scope="module")
def setup_once():
    return "Module Level Setup"

def test_1(setup_once):
    assert setup_once == "Module Level Setup"
    
def test_2(setup_once):
    assert setup_once == "Module Level Setup"