__author__ = 'Hernan Y.Ke'
from functools import wraps


# unwrap: remove the decorator

def dec1(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('1st decorator')
        return func(*args,**kwargs)
    return wrapper

def dec2(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('2nd decorator')
        return func(*args,**kwargs)
    return wrapper

@dec1
@dec2
def fun(x,y):
    return x+y
print(fun.__wrapped__(2,3))
print(fun.__wrapped__.__wrapped__(2,3))
#observe the order: