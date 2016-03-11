__author__ = 'Hernan Y.Ke'
from functools import partial
import math
def curry(a,b,c,d):
    print(a,b,c,d)

c1 = partial(curry,1)   #a=1   awful syntax...
c1(2,3,4)

c2=partial(curry,d=3) #d=3
c2(2,3,4)

c3=partial(curry,1,2,d=3)   #a=1 b=2 d=3
c3(5)

# my thought: when building a new function, all assigned params become default params.

def hyt(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.hypot(x2-x1,y2-y1)

pt = (4,3)

pts=[(1,2),(5,6),(5,9)]

pts.sort(key=partial(hyt,pt))       # cannot assign to another value:  newvar=pts.sort(key=partial(hyt,pt))
print(pts)


