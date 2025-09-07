""" 
Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.
A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y
For example, 123 is a seed of 738 as 123*1*2*3 = 738.
 
Sample Input
	
Expected Output


123,738
	
True


45,1000
	
False
 
"""

def is_seed(num1, num2):
    product = num1
    for digit in str(num1):
        product *= int(digit)
    print(f"Product of {num1} is : {product} and num2 is : {num2}")
    return product == num2

        

# Example usage
print(is_seed(123, 738))
print(is_seed(45, 1000))
print(is_seed(12, 24))
print(is_seed(5, 25))
print(is_seed(7, 49))