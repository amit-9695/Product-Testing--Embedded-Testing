import re
count = 0
pattern = re.compile("Python")
target_string = "Python is a programming language."     # Check if the pattern matches
mathcher = re.finditer(pattern, target_string)
print(mathcher)  
for match in mathcher:
    count= count + 1
    print(match.start(),"--->", match.end(),"---->", match.group())