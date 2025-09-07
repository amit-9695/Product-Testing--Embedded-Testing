# key() and values()

d= {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}

for key in d:   
    print(key," : ", d[key])  # Output: name --> Alice, age --> 25, city --> Los Angeles
    

print("Keys:", d.keys())  # Output: dict_keys(['name', 'age', 'city'])
print("Values:", d.values())  # Output: dict_values(['Alice', 25, 'Los Angeles'])
print("Items:", d.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'Los Angeles')])