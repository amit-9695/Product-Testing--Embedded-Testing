# Updating the value of a key 
# 1. Update an existing key's value
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Before update:", dict1)
dict1['age'] = 31 
print("After update:", dict1) 
print("=========================================>")

# 2. Add a new key-value pair
dict1['country'] = 'USA'
print("After adding new key-value pair:", dict1)
print("=========================================>")

# 3. Update multiple keys at once
dict1.update({'name': 'Alice', 'city': 'Los Angeles'})
print("After updating multiple keys:", dict1)
print("=========================================>")

# 4. Using setdefault() to update or add a key-value pair
dict1.setdefault('age', 25) 
print("After setdefault (age):", dict1)