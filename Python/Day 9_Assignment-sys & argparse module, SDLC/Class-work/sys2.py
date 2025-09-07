# Exiting the program
import sys

if len(sys.argv)!=2:
    print("Usage: python sys2.py <name>")
    sys.exit(1)
    
print("Hello", sys.argv[1])