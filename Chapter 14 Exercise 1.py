#  A decorator function that calculates the time to run a function
import math
import time
from functools import wraps
def decorator_func(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        print (f"Executing...{func.__name__}")
        t1= time.time()
        returned_value=(f"The sum is {func(*args,**kwargs)[0]}")
        t2= time.time()
        print(f"The function took {t2-t1} second to run")
        return returned_value
    return wrapper_func

@decorator_func
def basic_operations(operation,*args):
    return [sum(i) if operation=="sum" else math.prod(i) for i in args]

print(basic_operations(sum,[2,3,4]))