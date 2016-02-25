__author__ = 'Hernan Y.Ke'
from collections import defaultdict

d = defaultdict(list)

d['a'].append('a1')
d['a'].append('a2')
print(d)


#regular dict

dict = {}
dict.setdefault('a',[]).append('a1')
dict.setdefault('a',[]).append('a2')
print(dict)