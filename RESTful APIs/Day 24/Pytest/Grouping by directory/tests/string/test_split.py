import pytest

def test_split():
    assert "hello world".split() == ["hello", "world"]
    assert "a,b,c".split(",") == ["a", "b", "c"]
    assert "one two three".split() == ["one", "two", "three"]
    assert "   spaced   ".split() == ["spaced"]
    assert "test".split("e") == ["t", "st"]