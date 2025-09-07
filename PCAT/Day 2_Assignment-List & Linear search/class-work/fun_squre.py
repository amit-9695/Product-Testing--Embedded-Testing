# Squre of a number using function
# Taking input from user and printing the square of the number
num=int(input("Enter a number to find its square: "))
def square(num):
    """Returns the square of a number."""
    return num ** 2

result = square(num)
print(f"The square of 5 is: {result}")
