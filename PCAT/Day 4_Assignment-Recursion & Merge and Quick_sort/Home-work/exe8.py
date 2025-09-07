# Reverse a string
def reverse_string(s):
    if s == "":
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  
