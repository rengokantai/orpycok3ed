__author__ = 'Hernan Y.Ke'
import time
from functools import wraps
from inspect import signature

# equalto timethis(wrapper)
def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)      #outer function call inner function's args.
        end = time.time()
        print(func.__name__,end-start)
        return result
    return wrapper

@timethis
def cd(n:int):
    '''
    doc
    '''
    while n>0:
        n-=1
        print(n)

cd(5)
print(cd.__name__)
print(cd.__doc__)
print(cd.__annotations__)

# access wrapped function

cd.__wrapped__(5)
print(signature(cd))