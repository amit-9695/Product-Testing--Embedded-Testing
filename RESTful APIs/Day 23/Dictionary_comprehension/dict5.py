#  using zip() function in dictionary comprehension
#  zip two lists to create a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
zipped_dict = {k: v for k, v in zip(keys, values)}
print(zipped_dict)