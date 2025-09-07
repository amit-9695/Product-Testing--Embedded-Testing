from functools import reduce

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

c=reduce(add, range(1, 11))
d=reduce(mul, range(1, 11))
print("Sum of numbers from 1 to 10:", c)
print("Product of numbers from 1 to 10:", d)
