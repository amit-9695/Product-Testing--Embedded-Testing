def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    
g= mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

try:
    print(next(g))
except StopIteration:
    print("No more items to yield.")