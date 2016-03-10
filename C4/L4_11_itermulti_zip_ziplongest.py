__author__ = 'Hernan Y.Ke'
from itertools import zip_longest

arr1=[1,2,3,4]
arr2=[5,6,7]

for i in zip_longest(arr1,arr2):    # NOT  for i,j in....  no.
    print(i)

print('--')

for i in zip_longest(arr1,arr2,fillvalue=0):    #add default fillvalue
    print(i)


#make dict:

dict1 = dict(zip_longest(arr1,arr2,fillvalue=0))
print(dict1)

for i,j in zip_longest(arr1,arr2):    # for i,j in....  altertive syntax. can create customized output
    print(i, j)

# zip output is iterable, must convert to list.
print(zip(arr1,arr2))
print(list(zip(arr1,arr2)))
