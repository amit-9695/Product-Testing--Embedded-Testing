from utils import fizzbuzz

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def test_fizzbuzz_fizz():
    assert fizzbuzz(9) == "Fizz"

def test_fizzbuzz_buzz():
    assert fizzbuzz(10) == "Buzz"

def test_fizzbuzz_number():
    assert fizzbuzz(7) == "7"
