# Write a  Python program to square and cube every number in a given list of integers using Lambda.
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_list = list(map(lambda x: x ** 2, original_list))
cubed_list = list(map(lambda x: x ** 3, original_list))
print("Original List:", original_list)
print("Squared List:", squared_list)
print("Cubed List:", cubed_list)