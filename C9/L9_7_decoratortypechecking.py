__author__ = 'Hernan Y.Ke'
from inspect import signature
from functools import wraps

def type(*args,**kwargs):
    def decorate(func):
        if not __debug__:
            return func
        sig = signature(func)
        boundtype = sig.bind_partial(*args,**kwargs).arguments          #new API
        @wraps(func)
        def wrapper(*args,**kwargs):
            bound_value = sig.bind(*args,**kwargs)                      # another API
            for name,value in bound_value.argument.items():
                if name in boundtype:
                    if not isinstance(value,bound_value[name]):
                        raise TypeError('{} must be {}'.format(name,bound_value[name]))
            return func(*args,**kwargs)
        return wrapper
    return decorate

