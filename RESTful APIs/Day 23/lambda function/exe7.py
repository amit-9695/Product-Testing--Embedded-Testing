""" 
Write a  Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False

"""

string_check = lambda s, c: s.startswith(c)
print(string_check("hello", "h"))
print(string_check("world", "h"))
print(string_check("python", "p"))
print(string_check("lambda", "l"))
print(string_check("function", "f"))    
