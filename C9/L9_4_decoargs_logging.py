__author__ = 'Hernan Y.Ke'
from functools import wraps
import logging
"""
@decorator(x,y,z)
def d(a,b)
    return a+b

this is same as decorator(x,y,z)(d)
"""
# note the difference to L9_2, with one more layer of function
def logged(level, name=None, mes=None):
    def decorate(func):
        ln = name if name else func.__module__
        log = logging.getLogger(ln)
        logmsg = mes if mes else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level,logmsg)
            return  func(*args, **kwargs)
        return wrapper
    return decorate


#usage:

@logged(logging.DEBUG)
def add(x,y):
    return x+y

@logged(logging.CRITICAL,'mes')
def p():
    print("p")


p()
add(3,2)