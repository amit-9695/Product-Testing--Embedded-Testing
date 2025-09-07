# # Ask a person for a number between 1 and 100, ask again if they give you a number outside that range
number = int(input("Please enter a number between 1 and 100: "))
while number < 1 or number > 100:
    number = int(input("Invalid input. Please enter a number between 1 and 100: "))
print(f"You entered a valid number: {number}")
