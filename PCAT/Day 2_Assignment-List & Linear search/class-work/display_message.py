""" Implement a program that displays a message for a given number based on the below conditions.
If the number is a multiple of 3, display "Zip".
If the number is a multiple of 5, display "Zap".
If the number is a multiple of both 3 and 5, display "Zoom",
For all other cases, display "Invalid".
 """

def display(num):
    if num%3==0:
        if num%5==0:
            return "Zoom"
        return "Zip"
    elif num%5==0:
        return "Zap"
    else:
        return "Invalid"

num = int(input("Enter a number: "))
res=display(num)
print(res)
