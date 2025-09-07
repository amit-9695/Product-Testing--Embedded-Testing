# Grouping by Test files
import pytest

def test_uppercase():
    assert "hello".upper() == "HELLO"
    
def test_lowercase():
    assert "WORLD".lower() == "world"
    
def test_split():
    assert "hello world".split() == ["hello", "world"]