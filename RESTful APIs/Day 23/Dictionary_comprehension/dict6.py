# using string method
# count characters
string = "banana"
char_count = {char: string.count(char) for char in set(string)}
print(char_count)