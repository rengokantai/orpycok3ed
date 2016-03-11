__author__ = 'Hernan Y.Ke'
import sys
from timeit import timeit
#basic examp:

def maindef():
    n=0
    def func():
        print(n)

    def getn():
        return n
    def setn(val):
        nonlocal n
        n=val

    func.getn=getn
    func.setn=setn
    return func

m = maindef()
m()
m.setn(5)
print(m.getn())



#advanced
class CloIns:
    def __init__(self,locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((key,value)for key,value in locals.items())
    def __len__(self):
        return self.__dict__['__len__']()

def Stack1():
    items=[]
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    def __len__():
        return len(items)
    return CloIns()


#traditional way:
class Stack2():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

print('-----')
t = Stack1()
t.push(4)
print(len(t))
t.pop()
print(len(t))
del t

print('----perf test----')

st1 = Stack1()
print(timeit('st1.push(1);st1.pop()','from __main__ import st1'))
st2 = Stack2()
print(timeit('st2.push(1);st2.pop()','from __main__ import st2'))