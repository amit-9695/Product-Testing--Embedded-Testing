""" .Write a python program to find and display the product of three positive integer values based on the rule mentioned below:
It should display the product of the three values except when one of the integer values is 7. In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1
Note: Assume that if 7 is one of the positive integer values, then it will occur only once. Refer to the sample I/O given below.
 """
 
num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))    
num3 = int(input("Enter third positive integer: "))
def products_of_three(num1, num2, num3):
    if num1 !=7 and num2 != 7 and num3 != 7:
        return num1 * num2 * num3
    elif num1 == 7 and num2 != 7 and num3 != 7:
        return num2 * num3
    elif num1 != 7 and num2 == 7 and num3 != 7:
        return num1 * num3
    elif num1 == 7 and num2 == 7 and num3 != 7:
        return num3
    else:
        return -1
    
result = products_of_three(num1, num2, num3)
print("Result:", result)
    