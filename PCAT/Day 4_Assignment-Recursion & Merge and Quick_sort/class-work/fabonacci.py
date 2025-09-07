# Problem: Write a function that returns the nth Fibonacci number using recursion.
# Example Input: 6 → Output: 8

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print("Fibonacci of 5 is:", fib(6))