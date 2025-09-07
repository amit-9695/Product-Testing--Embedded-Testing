# Group by test file for math operations

# Test addition
def test_addition():
    assert 2 + 3 == 5
    
# Test subtraction
def test_subtraction():
    assert 5 - 3 == 2
    
# Test multiplication
def test_multiplication():
    assert 4 * 2 == 8
    
# Test division
def test_division():
    assert 10 / 2 == 5


# Note: To run these tests, you would open a terminal, navigate to the directory containing this file, and run: pytest test_math_operations.py or simply `pytest'.