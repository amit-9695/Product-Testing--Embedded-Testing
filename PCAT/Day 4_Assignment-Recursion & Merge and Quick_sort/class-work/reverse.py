# Problem: Write a function that prints numbers from n to 1 using recursion.
# Example Input: 5 → Output: 5 4 3 2 1

def rev(n):
    if n == 0:
        return 0
    print(n)
    rev(n - 1)
print(rev(125))
