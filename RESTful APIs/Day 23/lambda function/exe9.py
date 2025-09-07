""" 
Write a python program to generate a function to get the power of a specified number.

The output is:

Power of: 5, 6, 7
Specified number: 3

Expected Answer:
The power of five for number 3 = 15
The power of six for number 3 = 18
The power of seven for number 3 = 21

"""
def power_of_specified_number(power):
    return lambda x: x * power
specified_number = 3
power_of_five = power_of_specified_number(5)
power_of_six = power_of_specified_number(6)
power_of_seven = power_of_specified_number(7)
print(f"The power of five for number {specified_number} = {power_of_five(specified_number)}")
print(f"The power of six for number {specified_number} = {power_of_six(specified_number)}")
print(f"The power of seven for number {specified_number} = {power_of_seven(specified_number)}")