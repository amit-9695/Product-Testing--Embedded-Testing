# Check if a string is a palindrome (case-insensitive)
def is_palindrome(s):
    s = s.lower()
    if len(s) < 2:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("RaceCar"))  # True
print(is_palindrome("Hello"))     # False
