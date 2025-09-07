# Find the greatest common divisor (GCD) with Euclid’s algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  
