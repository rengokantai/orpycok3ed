__author__ = 'Hernan Y.Ke'
import math
class LazyA:
    def __init__(self,prop):
        self.prop=prop

    def __get__(self, instance,cls):
        if instance is None:
            return self
        else:
            val = self.prop(instance)       #this line is hardest line to memorize
            setattr(instance,self.prop.__name__,val)
            return val

class B:
    def __init__(self,ra):
        self.ra = ra
    @LazyA
    def area(self):
        print('area')
        return math.pi *self.ra**2

    @LazyA
    def peri(self):
        print('perimeter')
        return 2*math.pi*self.ra


c = B(100)
print(c.area)
print(c.area)
print(vars(c))
del c.area
print(vars(c))
print(c.area)