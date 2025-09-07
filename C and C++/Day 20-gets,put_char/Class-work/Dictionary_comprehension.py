# {Key:value for item in itrable}
# {key: value for item in iterable if condition}

squre={i:i*i for i in range(5)}
print(squre)

even_squares = {i: i * i for i in range(10) if i % 2 == 0}
print(even_squares)