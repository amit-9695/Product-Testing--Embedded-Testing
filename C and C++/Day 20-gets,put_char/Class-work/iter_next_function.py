# an iterator is an object that contains a countable number of values and can be iterated upon.

# __iter_() : return the iterator object itself.
# __next__() : returns the next value from the iterator. If there are no more

nums= [1, 2, 3, 4, 5]
iterator = iter(nums)
# values to return, it raises StopIteration exception.
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
print("<=======================================================>")

# Creating a custom iterator class
class MyIterator:
    def __init__(self, max):
        self.max = max
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.max:
            result = self.index
            self.index += 1 
            return result
        else:
            raise StopIteration()
        
# Using the custom iterator
my_iter = MyIterator(5)
for value in my_iter:
    print(value)  # Output: 0, 1, 2, 3, 4