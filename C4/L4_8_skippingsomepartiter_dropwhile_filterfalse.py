__author__ = 'Hernan Y.Ke'

from itertools import dropwhile,filterfalse

it1 = iter([1,2,3,4,5,6])

for i in dropwhile(lambda i:i<5,it1):
    print(i)

it2 = iter([1,2,3,4,5,6])
for i in filterfalse(lambda i:i%2==1,it2):
    print(i)