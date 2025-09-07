import pytest
from convert import c_to_f

@pytest.mark.parametrize(
    "cel,exp_fah",
    [
        (0, 32.00),
        (100, 212.00),
        (-40, -40.00),
        (37, 98.6),
        (25, 77.00)

    ]
)

def test_c_to_f(cel,exp_fah):
    assert c_to_f(cel)==exp_fah