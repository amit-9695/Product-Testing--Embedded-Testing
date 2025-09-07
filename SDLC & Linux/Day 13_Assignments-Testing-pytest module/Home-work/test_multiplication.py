def multiply(a,b):
    return a * b

# This is a simple test for a multiplication function
def test_multiply():
    actual = multiply(2, 3)
    expected = 6
    assert actual == expected
    print("Test passed!")