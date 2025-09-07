# Remove duplicates from dictionary (based on values)
#  display unique values only
original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
unique_values = {k: v for k, v in original_dict.items() if list(original_dict.values()).count(v) == 1}
print(unique_values)
print("<==========================================>")

# To display all values only once(no duplicates)
data = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
unique = {}
[unique.setdefault(v, k) for k, v in data.items()]
unique_dict = {v: k for k, v in unique.items()}
print(unique_dict)
print("<==========================================>")