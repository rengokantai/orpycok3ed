__author__ = 'Hernan Y.Ke'
from itertools import permutations,combinations,combinations_with_replacement

arr=['a','b','c']

for i in combinations(arr,2):#second params is mandatory
    print(i)

for i in permutations(arr,2):#second params is NOT mandatory
    print(i)


for i in combinations_with_replacement(arr,2):#second params is mandatory
    print(i)