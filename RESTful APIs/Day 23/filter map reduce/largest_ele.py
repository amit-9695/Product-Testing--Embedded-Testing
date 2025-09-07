# program that return the largest element in a non-empty list
from functools import reduce
def largest_element(lst):
    return reduce(lambda x, y: x if x > y else y, lst)

# Example usage
lst = [3, 5, 2, 8, 1]
largest = largest_element(lst)
print("The largest element in the list is:", largest)