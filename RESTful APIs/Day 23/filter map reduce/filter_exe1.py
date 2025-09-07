# create a filter function to filter out that the given list is divisible by 3
def filter_divisible_by_three(numbers):
    return list(filter(lambda x: x % 3 == 0, numbers))
# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter_divisible_by_three(numbers)
print("Numbers divisible by 3:", filtered_numbers)