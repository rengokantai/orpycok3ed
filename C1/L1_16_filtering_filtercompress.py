__author__ = 'Hernan Y.Ke'

from itertools import compress

# 1. using list comprehension

arr = range(1,10)


print(x for x in list(arr) if x %2==0)  #still fails.

pos = (x for x in list(arr) if x %2==0)  #must add parentheses

for x in pos:
    print(x)


# 2.using filter

def is_even(val):
    try:
        return val%2
    except:
        return False

res = list(filter(is_even,arr))  #filter returns generator.      note the position of param  function, arr
print(res)

# 3.using compressor

fil = [n%2 for n in arr]
print(list(compress(arr,fil)))      #note the position of param.   arr , placeholder