__author__ = 'Hernan Y.Ke'
from functools import wraps

class A:
    fs = property()
    def deco1(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('instance method decorator')
            return func(*args, **kwargs)
        return wrapper
    @classmethod
    def deco2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('class method decorator')
            return func(*args,**kwargs)
        return wrapper

a=A()

@a.deco1
def insdec():
    pass

@A.deco2        #using class.decoratorname
def clsdec():
    pass

insdec()
clsdec()



class B:
    f = property()

    @f.getter
    def f(self):
        return self._f
    @f.setter
    def f(self,val):
        if not isinstance(val,str):
            raise TypeError('string!')
        self._f=val

