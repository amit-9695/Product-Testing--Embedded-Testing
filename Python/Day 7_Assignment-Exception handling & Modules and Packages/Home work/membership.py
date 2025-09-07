# Checking membership in a dictionary
# 1. Check if a key exists in the dictionary

d = {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
print('name' in d)  
print('country' in d)  
print("=========================================>")

# 2. Check if a value exists in the dictionary
print('Alice' in d.values())  
print('USA' in d.values())  
print("=========================================>")

# 3. Using the keys() method to check for a key
print('age' in d.keys())  
print('country' in d.keys())  
print("=========================================>")
# 4. Using the get() method to check for a key with a default value
print(d.get('name', 'Not Found')) 
print(d.get('country', 'Not Found'))  


# 5. Using the items() method to check for a key-value pair
print(('name', 'Alice') in d.items())  # Output: True
print(('country', 'USA') in d.items())  # Output: False
print("=========================================>")