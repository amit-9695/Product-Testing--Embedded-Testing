# print the multiplication table of a number
num = int(input("Enter a number for multiplication table: "))
print(f"Multiplication table of {num} is:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
