#  Retriving the values in dictionary
# There are two methods to retriving the value from the dictonary:- 1. Using key;   # 2. Using get() method
# 1. Using key
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
print(dict1['name'])  # Output: John


# 2. Using get() method
print(dict1.get('age'))  # Output: 30
# 3. Using get() method with default value
print(dict1.get('country', 'USA'))  # Output: USA (default value since 'country' key does not exist)
# 4. Using get() method with a key that does not exist
print(dict1.get('country'))  # Output: None (no default value provided)
