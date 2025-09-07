# A parameterized fixture allows a fixture to run multiple times with different input values.
# @pytest.fixture(params=[....])

import pytest

@pytest.fixture(params=[1,2,3])
def number(request):
    return request.param

def test_is_even(number):
    print(f"Testing with : {number}")
    assert number%2==0

@pytest.fixture(params=[
    (2,4),
    (3,9),
    (4,16)
])
def number_pair(request):
    return request.param

def test_square(number_pair):
    num,expected=number_pair
    assert num**2==expected
