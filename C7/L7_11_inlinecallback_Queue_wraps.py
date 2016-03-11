__author__ = 'Hernan Y.Ke'
from queue import Queue
from functools import wraps

def applyasync(func,args,*,cb):
    res=func(*args)
    cb(res)

class Async:
    def __init__(self,func,args):
        self.func = func
        self.args=args

def inlined(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        res_que=Queue()
        res_que.put(None)
        while True:
            res = res_que.get()
            try:
                a=f.send(res)
                applyasync(a.func,a.args,cb=res_que.put)
            except StopIteration:
                break
    return wrapper


def add(x,y):
    return x+y


@inlined
def test():
    r = yield Async(add,(1,2))
    print(r)
    for n in range(3):
        r = yield Async(add,(n,n))
        print(r)

test()