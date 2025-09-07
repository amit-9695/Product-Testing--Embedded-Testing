# range and union Regex character classes

import re
#RegEx pattern
pattern = '[^a-zA-Z0-9]'
matcher=re.finditer(pattern,"abcdeyABZ12#$%")
for match in matcher:
    print(match.start(),"...",match.end(),"...",match.group())