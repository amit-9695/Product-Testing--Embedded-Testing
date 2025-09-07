# Reading from standard input

import sys
print("Enter something: ")
for line in sys.stdin:
    if line.strip() == "exit":
        break
    print("You typed: ", line.strip())