from functools import wraps

def decoratorfunc(func):
    @wraps(func)
    def wraper():
        print("Before function runs")
        func()
        print("After function runs")

    return wraper

@decoratorfunc
def greet():
    print("Hello this is the function that would run after the decorator before statement")
@decoratorfunc
def window():
    print("I dont know what will happen to this function")

window()
greet()

print(greet.__name__)