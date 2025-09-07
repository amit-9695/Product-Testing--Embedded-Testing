# parametrize marker - Run the same test with multiple sets of parameters
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30),
    (-1, 1, 0),
    (0, 2, 2),
    (3.5, 2.5, 6.0)
])

def test_addition(a, b, expected):
    assert a + b == expected