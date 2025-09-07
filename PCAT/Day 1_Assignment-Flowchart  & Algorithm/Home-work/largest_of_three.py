num1=33
num2=44
num3=55
if num1 > num2 and num1 > num3:
    print("Largest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("Largest number is:", num2)
elif num3 > num1 and num3 > num2:
    print("Largest number is:", num3)
else:
    print("All numbers are equal")
    