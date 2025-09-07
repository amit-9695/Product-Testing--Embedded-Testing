# Question Number 2   
import re

def is_strong_password(password):
    if len(password) < 8:
        return False

    pattern = (
        r"^(?=.*[A-Z])"
        r"(?=.*[a-z])"
        r"(?=.*\d)"
        r"(?=.*[!@#$%^&*(),.?\":{}|<>])"
        r".+"
        r"$"
    )

    return bool(re.search(pattern, password))

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")

    if is_strong_password(user_password):
        print(f"Result: '{user_password}' is a STRONG password.")
    else:
        print(f"Result: '{user_password}' is a WEAK password. "
              "A strong password needs at least 8 characters, an uppercase letter, "
              "a lowercase letter, a number, and a special character.")

