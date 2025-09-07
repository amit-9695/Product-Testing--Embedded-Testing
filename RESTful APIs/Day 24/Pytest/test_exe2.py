# Testing Exceptions in Pytest
import pytest
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
    assert divide(10, 2) == 5.0
    assert divide(-6, 3) == -2.0
    assert divide(7.5, 2.5) == 3.0
    assert divide(0, 1) == 0.0