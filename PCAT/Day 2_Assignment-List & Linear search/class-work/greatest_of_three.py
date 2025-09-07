# Finding the greatest of three numbers using function

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def greatest(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3

result = greatest(num1, num2, num3)
print(f"The greatest number among {num1}, {num2}, and {num3} is: {result}")