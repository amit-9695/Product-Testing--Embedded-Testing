""" 
Write a  Python program to create a lambda function,
that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and prints the result.
"""

lambda_add = lambda x: x + 15
print("Adding 15 to 10 gives:", lambda_add(10))
print("Adding 15 to 20 gives:", lambda_add(20))

lambda_multiply = lambda x, y: x * y
print("Multiplying 5 and 10 gives:", lambda_multiply(5, 10))
print("Multiplying 3 and 7 gives:", lambda_multiply(3, 7))