# Count occurrences of a character c in string s
def count_char(s, c):
    if s == "":
        return 0
    return (1 if s[0] == c else 0) + count_char(s[1:], c)

print(count_char("hello", "l"))  
