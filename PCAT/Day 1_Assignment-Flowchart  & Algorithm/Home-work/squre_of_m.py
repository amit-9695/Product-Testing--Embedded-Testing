# Input M and print the square of M if it is between 1 and 10.
M = int(input("Enter a number M: "))
if 1 <= M <= 10:
    print("The square of M is:", M ** 2)
else:
    print("M is out of range.")
