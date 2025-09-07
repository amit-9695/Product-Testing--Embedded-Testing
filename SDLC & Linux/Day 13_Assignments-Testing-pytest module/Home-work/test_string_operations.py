# Group by test file for string operations

# Test string concatenation
def test_string_concatenation():
    assert "Hello" + " " + "World" == "Hello World"

# Test string length
def test_string_length():
    assert len("Hello") == 5

# Test string uppercase
def test_string_uppercase():
    assert "hello".upper() == "HELLO"

# Test string lowercase
def test_string_lowercase():
    assert "HELLO".lower() == "hello"
    
# Test string split
def test_string_split():
    assert "Hello World".split() == ["Hello", "World"]

# Note: To run these tests, you would open a terminal, navigate to the directory containing this file, and run: pytest test_string_operations.py or simply `pytest`.