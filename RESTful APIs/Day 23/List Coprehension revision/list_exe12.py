# Creating a table from 1 to 10 using list comprehension
table = [[i * j for i in range(1, 11)] for j in range(1, 11)]
print(table)