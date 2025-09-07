# Problem: Write a function to calculate the sum of first n natural numbers.
# Example Input: 4 → Output: 10 (1 + 2 + 3 + 4)

def sum_natural(num):
    if num ==0:
        return 0
    else:
        return num + sum_natural(num-1)
    
num = int(input("Enter a natural number: "))
sum= sum_natural(num)
print("Sum of natural numbers up to", num, "is:", sum)