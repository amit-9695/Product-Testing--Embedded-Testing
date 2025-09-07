#1. using "{" to create a dictionary
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
print(dict1)  
print("=========================================>")

#2. using dict() constructor to create a dictionary
dict2 = dict(name='Alice', age=25, city='Los Angeles')
print(dict2)
print("=========================================>")

#3. using zip() function to create a dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Bob', 22, 'San Francisco']
dict3 = dict(zip(keys, values))
print(dict3)
print("=========================================>")

#4. using dictionary comprehension to create a dictionary
dict4 = {key: value for key, value in zip(keys, values)}
print(dict4)
print("=========================================>")

#5. using list of tuples to create a dictionary
dict5 = dict([('name', 'Charlie'), ('age', 28), ('city', 'Chicago')])
print(dict5)    
print("=========================================>")

#6. using eval() to create a dictionary from a string representation
d = eval("{'name': 'David', 'age': 35, 'city': 'Miami'}")
print(d)
print("=========================================>")

#7. using fromkeys() method to create a dictionary with default values
keys = ['a', 'b', 'c']
default_value = 0
dict6 = dict.fromkeys(keys, default_value)
print(dict6)
print("=========================================>")

#8 using a list of key-value pairs to create a dictionar
d=dict([('a', 1), ('b', 2), ('c', 3)])
print(d)