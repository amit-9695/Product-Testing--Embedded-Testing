# Implement a program to display the sum of two given numbers if the numbers are same. If the numbers are not same, display the double of the sum.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
def operation_on_numbers(num1, num2):
    if num1 == num2:
        return num1 + num2
    else:
        return 2 * (num1 + num2)

result = operation_on_numbers(num1, num2)
print("Result:", result)