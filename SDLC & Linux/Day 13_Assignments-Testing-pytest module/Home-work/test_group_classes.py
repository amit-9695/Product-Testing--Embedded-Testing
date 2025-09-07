# Grup by classes

#creatiing a class for math operations tests
class TestMathOperations:
    # Test addition
    def test_addition(self):
        assert 2 + 3 == 5

    # Test subtraction
    def test_subtraction(self):
        assert 5 - 3 == 2

    # Test multiplication
    def test_multiplication(self):
        assert 4 * 2 == 8

    # Test division
    def test_division(self):
        assert 10 / 2 == 5
        
        
# creating a class for string operations tests
class TestStringOperations:
    # Test string concatenation
    def test_string_concatenation(self):
        assert "Hello" + " " + "World" == "Hello World"

    # Test string length
    def test_string_length(self):
        assert len("Hello") == 5

    # Test string uppercase
    def test_string_uppercase(self):
        assert "hello".upper() == "HELLO"

    # Test string lowercase
    def test_string_lowercase(self):
        assert "HELLO".lower() == "hello"
    
    # Test string split
    def test_string_split(self):
        assert "Hello World".split() == ["Hello", "World"]
        
        
# Note: To run these tests, you would open a terminal, navigate to the directory containing this file, and run: pytest test_group_classes.py or simply `pytest`.

# Note: To run any specific test class, you can use the command: pytest test_group_classes.py::TestMathOperations or pytest test_group_classes.py::TestStringOperations 