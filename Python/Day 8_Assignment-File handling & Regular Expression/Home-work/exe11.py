import re
#is ametacharacter that specifies that the preceding character or group is optional
#Compile a regular expression pattern, returning a Pattern object.
pattern=re.compile(r'(\d{1,2})-(\d{1,2})-(\d{4})')
#data to search in..
data="31-08-1234"

#Return a list of all non-overlapping matches in the string.
match_iter=re.finditer(pattern,data)

for match in match_iter:
    print(match.start(),match.end(),match.group())
