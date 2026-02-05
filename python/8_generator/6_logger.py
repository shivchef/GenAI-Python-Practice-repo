#How to create logger
from functools import wraps
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):   
        print(f"Calling: {func.__name__}")    #*args and **kwargs will get whatever values that are passed from the function
        result = func(*args,**kwargs)
        print(f"finished calling: {func.__name__}")
        return result
    return wrapper
@log_activity
def brew_chai(type, milk = 'no'):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("masala")