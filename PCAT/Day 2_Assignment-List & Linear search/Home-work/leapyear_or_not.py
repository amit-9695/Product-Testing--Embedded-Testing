# Checking the leap year or not
# leap year is a year that is divisible by 4, except for end-of-century years (100), unless they are divisible by 400.

year=int(input("Enter a Year:"))

def is_leap_year(year):
    """Returns True if the year is a leap year, otherwise False."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

result = is_leap_year(year)
if result:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")