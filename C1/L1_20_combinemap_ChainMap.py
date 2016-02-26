__author__ = 'Hernan Y.Ke'
from collections import ChainMap

a = {
    'A': 100,
    'B': 10}
b={
    'B': 20,
    'D': 50
}

c = ChainMap(a,b)   # Check first map first Do c['B']=10
print(list(c.keys()))  # ABD
print(list(c.values()))    #100 10 50
#del c['D']  #can not delete key in first map

#others.  new_child merge, update

val = ChainMap()
val['x']=1
val = val.new_child()
val['x']=2
val = val.new_child()
val['x']=3
print(val)
print(val['x'])

val=val.parents
print(val['x'])
val=val.parents
print(val['x'])
print(val)

#=========

c = {
    'A': 100,
    'B': 10}
d={
    'B': 20,
    'D': 50
}

merged = dict(d)
merged.update(c)
print(merged['B']) #still 10
c['A']=200
print(merged['A']) #still 100 because merged is a new copy

merged=ChainMap(c,d)
print(merged['A'])
c['A']=300
print(merged['A']) #300 because child change parent's value

