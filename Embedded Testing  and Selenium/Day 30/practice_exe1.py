""" 
Write a Python function which generates and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.
 
Sample Input 
10
	
Expected Output
	
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

"""

def generate_square_dict(n):
    square_dict = {i: i**2 for i in range(1, n+1)}
    return square_dict

# Sample usage
n=int(input("Enter a number: "))
result = generate_square_dict(n)
print(result)