# Problem: Calculate x raised to power n using recursion.
# Example Input: power(2, 3) → Output: 8

def power(base,exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = power(base, exp)
print(f"{base} raised to the power of {exp} is: {result}")