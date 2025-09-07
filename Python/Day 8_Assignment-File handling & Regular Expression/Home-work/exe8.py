# re module
import re
count=0
pattern=re.compile("python")
matcher=pattern.finditer("python is a prog and python is High level")
for match in matcher:
    count+=1
    print(match.start(),"...",match.end(),"...",match.group())
    print("The number of occurrences: ",count)