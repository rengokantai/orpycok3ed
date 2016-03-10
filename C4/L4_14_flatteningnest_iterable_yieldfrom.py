__author__ = 'Hernan Y.Ke'
from collections import Iterable

def flatten(items,ignore=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable)and not isinstance(x,ignore):
            yield from flatten(x,ignore)
        else:
            yield x

arr=[1,[2,[3,4,5]]]

for x in flatten(arr):
    print(x)


#if not use yield from?
"""
def flatten(items,ignore=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable)and not isinstance(x,ignore):
            for i in flatten(x)
                yield i
        else:
            yield x
"""