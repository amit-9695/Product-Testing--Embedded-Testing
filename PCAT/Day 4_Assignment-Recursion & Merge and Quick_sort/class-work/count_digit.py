# Problem: Count the number of digits in a given number using recursion.
# Example Input: 12345 → Output: 5

def count_digit(num):
    if num==0:
        return 0
    return 1 + count_digit(num // 10)
num = int(input("Enter a number: "))
count = count_digit(num)
print("Number of digits in", num, "is:", count)