""" 
Write a python program to generate a function to double a specified number.

The output is:

Specified number: 27.2

Expected Answer:
The double number of 27.2 = 54.4
"""
double_number = lambda x: x * 2
specified_number = 27.2
result = double_number(specified_number)
print(f"The double number of {specified_number} = {result}")