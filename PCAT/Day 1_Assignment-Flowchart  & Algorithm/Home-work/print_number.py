# Input the number N, print the numbers from 1 to N 
N=int(input("Enter the number N:"))
 
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(N)
