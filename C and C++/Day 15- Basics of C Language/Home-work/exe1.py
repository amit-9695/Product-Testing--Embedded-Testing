# question 1
import re
import keyword

def is_valid_python_variable_name(name):
    if keyword.iskeyword(name): 
        return False
    return bool(re.fullmatch(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name))

var_name = input("Enter a string for variable name validation: ")
if is_valid_python_variable_name(var_name):
    print(f"'{var_name}' is a VALID Python variable name.")
else:
    print(f"'{var_name}' is NOT a valid Python variable name.")