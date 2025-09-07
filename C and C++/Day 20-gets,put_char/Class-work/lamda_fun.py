# Lambda function is a named function that can take any number of arguments but can only have one expression.
#Simple Function
# def function_name(parameters):
def squre(n):
    return n * n
res = squre(5)
print(res)
print("<=======================================================>")

# Lambda Function
# lambda parameters: expression
squ=lambda x: x * x
res=squ(5)
print(res)
print("<=======================================================>")

# Addition using lambda function
add=lambda x, y: x + y
print(add(5, 3))
print("<=======================================================>")

#Finding max of two numbers using lambda function
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  
print("<=======================================================>")


# Purform adition, subtraction, multiplication, and division using lambda functions
def calculate(x, y, operation):
    return operation(x, y)

add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"
print(calculate(10, 5, add))        
print(calculate(10, 5, subtract))
print(calculate(10, 5, multiply))
print(calculate(10, 5, divide))