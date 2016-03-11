__author__ = 'Hernan Y.Ke'

no_value = object()
def objobserve(a,b=no_value):
    if b is no_value:
        print('b not here')

objobserve(1,2)
objobserve(1,None)
objobserve(1)

# def obj(a,b=[]):   incorrect-> must be inmutable object.

# the values assigned as a default are bound only once at the time of the function def.

x=3
def printdef(a,b=x):
    print(a,b)

printdef(1)
x=2
printdef(1)