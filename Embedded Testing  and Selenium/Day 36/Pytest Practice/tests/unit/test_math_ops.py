import pytest
from src.math_ops import add, sub, mul, div
@pytest.mark.smoke
def test_add():
    assert add(2, 3) == 5
def test_sub():
    assert sub(10, 6) == 4
@pytest.mark.parametrize("a,b,expected", [
(2, 3, 6),
(-1, 5, 5),
(0, 7, 0),
])
def test_mul(a, b, expected):
    assert mul(a, b) == expected
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_div_by_zero():
    div(10, 0)
@pytest.mark.regression
def test_div():
    assert div(9, 3) == 3