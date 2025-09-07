# fiding the vowels in a string using filter and map
from functools import reduce
def number_of_vowels(string):
    return reduce(lambda x, y: x+y, map(string.lower().count, 'aeiou'))

string = "Hello World"
vowel_count = number_of_vowels(string)
print(f"Number of vowels in '{string}': {vowel_count}")
