__author__ = 'Hernan Y.Ke'

#inplement __reversed__ to use reversed function

class Func:
    def __init__(self,time):
        self.time= time

    def __iter__(self):
        n = self.time
        while n>0:
            yield n
            n-=1

    def __reversed__(self):
        n=1
        while n<=self.time:
            yield n
            n+=2

f = Func(8)
for i in f:
    print(i)

print('----')
for j in reversed(f):
    print(j)