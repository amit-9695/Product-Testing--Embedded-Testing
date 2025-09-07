import re
pattern=re.compile(r'a*b+\w+')
data="abb ac aaabbb aaa aaabbcc cc bb"

#Return a list of all non-overlapping matches in the string.
match_iter=re.finditer(pattern,data)

for match in match_iter:
    print(match.start(),match.end(),match.group())
