# Grouping by Markers- Markers allow you to label and run specific groups to tests.
import pytest

@pytest.mark.math
def test_add():
    assert 2 + 3 == 5
    
@pytest.mark.math
def test_subtract():
    assert 5 - 4 == 1
    
@pytest.mark.math
def test_multiply():
    assert 3 * 4 == 12
    
# Grouping by String Operations
@pytest.mark.string
def test_uppercase():
    assert "hello".upper() == "HELLO"

@pytest.mark.string
def test_lowercase():
    assert "WORLD".lower() == "world"
    
@pytest.mark.string
def test_split():
    assert "hello world".split() == ["hello", "world"]
    