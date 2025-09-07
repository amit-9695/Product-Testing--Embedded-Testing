# A decorator is use - If you want to add additional functionality withou altering the original function.
# Decorattor function takes a function as an argument and returns a new function that adds some kind of functionality.


def f1(a,b):
    print("This is the outer function")
    def f2():
        print("This is the Inner function")
        print("It can use the arguments of the outer function")
        return a + b
    return f2

res= f1(5, 10)
print(res())  
print("<=======================================================>")


# Decorator function
def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

# Using the decorator
@my_decorator
def say_hello():
    print("Hello, World!")
    
say_hello()  
print("<=======================================================>")


# Another example of a decorator
def decorator_function(func):
    def inner_function():
        result= func()
        return result * 2
    return inner_function

@decorator_function
def get_nuber():
    return 5

res=get_nuber()
print(res)  #