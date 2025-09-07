""" 
Write a  Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.
"""
multiply_with_double = lambda x: x * 2  
multiply_with_tripal = lambda x: x * 3  
multiply_with_quadruple = lambda x: x * 4  
multiply_with_quintuple = lambda x: x * 5  
print("Multiplying 15 with double gives:", multiply_with_double(15))
print("Multiplying 15 with triple gives:", multiply_with_tripal(15))
print("Multiplying 15 with quadruple gives:", multiply_with_quadruple(15))
print("Multiplying 15 with quintuple gives:", multiply_with_quintuple(15))


print("<========================================================================>")
# Another method to do the same, by using a function
def multiply_with_factor(n):
    return lambda x: x * n

double = multiply_with_factor(2)
triple = multiply_with_factor(3)
quadruple = multiply_with_factor(4)
quintuple = multiply_with_factor(5)
print("Multiplying 15 with double gives:", double(15))
print("Multiplying 15 with triple gives:", triple(15))
print("Multiplying 15 with quadruple gives:", quadruple(15))
print("Multiplying 15 with quintuple gives:", quintuple(15))