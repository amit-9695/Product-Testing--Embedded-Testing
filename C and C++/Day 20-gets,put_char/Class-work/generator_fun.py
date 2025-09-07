# A generator is a siplar way to create an iterator in Python.
# It is a function that uses the yield statement to return values one at a time, allowing iteration over a sequence of values without storing them all in memory at once.
# Generators are defined using the def keyword and can be used like any other iterator.
# Yield keyword inside a function is used to make it grnrator function.
def generator_name():
    # Statements
    yield 1
    yield 2
    yield 3
    
# Using the generator function
gen = generator_name()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

print("<=======================================================>")

# Another example of a generator function
def count_upto(num):
    for i in range(num):
        yield i
        
for number in count_upto(5):
    print(number) 