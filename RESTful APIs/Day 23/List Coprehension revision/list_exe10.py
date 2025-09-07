# Generating a list of prime numbers from 0 to 50 using list comprehension
primes = [x for x in range(51) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1]
print(primes)