# Group by marker

import pytest

# Test group marker for math operations
@pytest.mark.math_operations
def test_addition():
    assert 2 + 3 == 5
    
@pytest.mark.math_operations
def test_subtraction():
    assert 5 - 3 == 2
    
@pytest.mark.math_operations
def test_multiplication():
    assert 4 * 2 == 8

@pytest.mark.math_operations
def test_division():
    assert 10 / 2 == 5
    
    
    
# Test group marker for string operations
@pytest.mark.string_operations
def test_string_concatenation():
    assert "Hello" + " " + "World" == "Hello World"

@pytest.mark.string_operations
def test_string_length():
    assert len("Hello") == 5

@pytest.mark.string_operations
def test_string_uppercase():
    assert "hello".upper() == "HELLO"

@pytest.mark.string_operations
def test_string_lowercase():
    assert "HELLO".lower() == "hello"

@pytest.mark.string_operations
def test_string_split():
    assert "Hello World".split() == ["Hello", "World"]
    
# Note: To run these tests, you would open a terminal, navigate to the directory containing this file, and run: pytest -m math_operations or pytest -m string_operations

#Note: To register the custom markers, you can add the following to your pytest configuration file (pytest.ini):
""" The following is the content for pytest.ini file to register custom markers:
[pytest]
markers =
    math_operations: mark test as part of math operations
    string_operations: mark test as part of string operations 
    """