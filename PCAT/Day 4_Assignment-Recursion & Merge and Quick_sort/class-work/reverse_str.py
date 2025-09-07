# Problem: Write a recursive function that reverses a given string.
# Example Input: "hello" → Output: "olleh"

def rev_str(str):
    if len(str)==0:
        return str
    return rev_str(str[1:])+str[0]
str="AMIT"
rev=rev_str(str)
print(rev)