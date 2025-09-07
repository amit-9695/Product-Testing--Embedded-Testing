# Flattening a Nested List using List Comprehension
matrix=[[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list=[item for sublist in matrix for item in sublist]
print(flat_list)