# We can use character classes to search a group of characters
import re
#RegEx pattern
pattern = '[^abc]'
matcher=re.finditer(pattern,"abcdef")
for match in matcher:
    print(match.start(),"...",match.end(),"...",match.group())
