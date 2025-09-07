# generate fibonaccci sequence

def fibonacci_sequence(n):
    print("Generating Fibonacci sequence up to", n)
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
        
values = fibonacci_sequence(15)

for x in values:
    print(x)