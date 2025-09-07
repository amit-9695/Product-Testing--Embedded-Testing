# reduce(fun, iterable, initializer)
# To use reduce function, you need to import it from functools module
from functools import reduce

nums = [1, 2, 3, 4, 5]
# Using reduce to find the sum of all numbers in a list
sum_of_nums = reduce(lambda x, y: x + y, nums)
print(f"Sum of all the elemnets of list : ",sum_of_nums)
print("<=======================================================>")

# Finding minimum and maximum in a list using reduce
min_num = reduce(lambda x, y: x if x < y else y, nums)
max_num = reduce(lambda x, y: x if x > y else y, nums)
print("Minimum:", min_num)
print("Maximum:", max_num)