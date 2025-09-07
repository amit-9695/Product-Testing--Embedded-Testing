# checking that the number is buzz number or not
# Taking input from user and checking if the number is buzz number or not
num = int(input("Enter a number to check if it is a buzz number: "))
def is_buzz(num):
    if num % 10 == 7 or num % 7 == 0:
        return True
    else:
        return False

result = is_buzz(num)
if result:
    print(f"{num} is a buzz number.")
else:
    print(f"{num} is not a buzz number.")
