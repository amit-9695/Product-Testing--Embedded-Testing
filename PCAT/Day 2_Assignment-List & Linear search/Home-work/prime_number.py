# Checking if a number is prime or not

num = int(input("Enter any Number:"))

def is_prime(num):
    for i in range (2,num//2):
        if num % i == 0:
            return False
        else:
            return True
result = is_prime(num)
if result:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    