import re
pattern=re.compile(r'\d+')
data="marks are 90,45,67,333,21"

#Return a list of all non-overlapping matches in the string.
match_iter=re.finditer(pattern,data)

for match in match_iter:
    print(match.start(),match.end(),match.group())
