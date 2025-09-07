# *args: used to pass a variable number of positional arguments to a function.

def add_numbers(*args):
    add=sum(args)  
    print("Positional arguments:", add)
    
# Example usage
add_numbers(1, 2, 3)
add_numbers(4, 5, 6, 7, 8)
add_numbers(9)