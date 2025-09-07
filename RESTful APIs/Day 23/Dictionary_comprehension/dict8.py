# Enumerate with dictionary comprehension
# index to value mapping
colors = ['red', 'green', 'blue']
index_mapping = {index: color for index, color in enumerate(colors)}
print(index_mapping)