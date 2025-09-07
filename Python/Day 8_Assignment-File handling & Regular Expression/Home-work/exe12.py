import re
pattern=re.compile(r'(\b[A-Z]+\b).+(\b\d+\b)')

#data to search in..
data="The price of PINEAPPLE ice cream is 20"

#Return a list of all non-overlapping matches in the string.
match_iter=re.finditer(pattern,data)

for match in match_iter:
    print(match.start(),match.end(),match.group(2))
