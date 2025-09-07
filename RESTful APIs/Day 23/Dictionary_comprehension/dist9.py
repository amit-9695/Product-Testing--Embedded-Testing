# Reverse a dictionary
# Valur to key

original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original_dict.items()}
print(reversed_dict)
