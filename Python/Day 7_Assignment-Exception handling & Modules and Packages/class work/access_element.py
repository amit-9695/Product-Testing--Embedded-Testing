# 1. access element of dictionary using key
d = {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
print(d['name'])  # Output: Alice

# 2. access element of dictionary using get() method
print(d.get('age'))  # Output: 25


# key error example
#1. using key that does not exist
try:
    print(d['country'])  # This will raise a KeyError
except KeyError as e:
    print(f"KeyError: {e}")
    
# 2. using get() method with a default value
# Output: USA (default value since 'country' key does not exist)
print(d.get('country', 'USA'))  

# 3. An alternative way to deal with the problem. You could also check if the key is in the dictionary.
if 'country' in d:
    print(d['country'])
else:
    print("Key 'country' does not exist in the dictionary.")
    
 