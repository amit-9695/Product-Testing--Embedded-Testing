# Grouping by classes- You can group tests by classes, Classes should not have an __init__ method when using pytest
import pytest

class TestMathOperations:
    def test_add(self):
        assert 2 + 3 == 5
    def test_subtract(self):
        assert 5 - 4 == 1
    def test_multiply(self):
        assert 3 * 4 == 12
        
        
class TestStringOperations:
    def test_uppercase(self):
        assert "hello".upper() == "HELLO"
    def test_lowercase(self):
        assert "WORLD".lower() == "world"
    def test_split(self):
        assert "hello world".split() == ["hello", "world"]