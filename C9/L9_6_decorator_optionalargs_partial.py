__author__ = 'Hernan Y.Ke'
from functools import partial,wraps
import logging
def logged(func=None, *,level=logging.DEBUG,name=None,mes=None):
    if func is None:
        return partial(logged, level=level, name=name,mes=mes)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg =mes if mes else func.__name__
    @wraps(func)
    def wrapper(*args,**kwargs):
        log.log(level, logmsg)
        return func(*args,**kwargs)
    return wrapper

#usage

@logged
def add(x,y):
    return x+y

@logged(level=logging.CRITICAL,name="ex")
def printsm():
    print('tem')

print(add(3,5))
printsm()