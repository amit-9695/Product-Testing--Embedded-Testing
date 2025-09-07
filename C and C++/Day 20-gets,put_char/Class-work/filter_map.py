# Using map function
# map(fun, iterable)

# Mapping the square of numbers in a list
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)
print("<=======================================================>")


# Mapping a list string to find the uppercase letters
words = ["Hello", "world", "Python", "is", "awesome"]
uppercase_words = list(map(lambda s: s.upper(), words))
print(uppercase_words)