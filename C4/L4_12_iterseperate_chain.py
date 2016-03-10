__author__ = 'Hernan Y.Ke'
from itertools import chain
arr1=[1,2,3,4]
arr2=[5,6,7]

for i in chain(arr1,arr2):      #  for i in a+b  -> less efficient
    print(i)

