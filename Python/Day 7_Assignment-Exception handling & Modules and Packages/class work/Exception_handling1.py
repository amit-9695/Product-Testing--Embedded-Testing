try:
    num1=int(input("enter first number"))
    num2=int(input("enter second number"))
    div=num1/num2
    print(f"Div= {div}")
except ZeroDivisionError as e:
    print("div by zero is not allowed")
except ValueError as e:
    print("Please provide valid input")

print("Thanks for using app")
