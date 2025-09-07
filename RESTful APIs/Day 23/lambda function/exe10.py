""" 
Write a python program to generate a lambda function to check whether a given string is a number or not. (True or False)

The output is:

Example of Expected Answer:
Is the given 3687 a number: True
"""

def is_number(s):
    return lambda x: x.isdigit()

check_number = is_number("3687")
print(f"Is the given 3687 a number: {check_number('3687')}")
print(f"Is the given 'abc' a number: {check_number('abc')}")
print(f"Is the given '1234' a number: {check_number('1234')}")
print(f"Is the given '12.34' a number: {check_number('12.34')}")