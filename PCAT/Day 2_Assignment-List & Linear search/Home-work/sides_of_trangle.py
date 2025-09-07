""" Write a python function to check whether three given numbers can form the sides of a triangle. 
Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers. """

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
def is_sides_of_triangle(a, b, c):
    if (a < b + c) and (b < a + c) and (c < a + b):
        return True
    else:
        return False
result = is_sides_of_triangle(num1, num2, num3)
if result:
    print("The numbers can form the sides of a triangle.")
else:
    print("The numbers cannot form the sides of a triangle.")