def div(a,b):
    if (a<b):
        a,b=b,a
    print(a/b)
div(2,4)
a=2^4
print(a)
# A decorator is a design pattern in Python 
# that allows a user to add new functionality to an existing
#  object without modifying its structure.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
