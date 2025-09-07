# Conditional Transformation of elements in a list using list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformed = [i if i % 2 == 0 else -1 for i in numbers]
print(transformed)