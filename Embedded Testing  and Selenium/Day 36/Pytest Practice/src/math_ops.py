def add(a: int | float, b: int | float):
    return a + b

def sub(a: int | float, b: int | float):
    return a - b
def mul(a: int | float, b: int | float):
    return a * b
def div(a: int | float, b: int | float):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b