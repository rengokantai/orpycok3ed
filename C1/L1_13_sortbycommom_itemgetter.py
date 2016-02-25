__author__ = 'Hernan Y.Ke'

from operator import itemgetter

items = [{'first': 'Hernan', 'last': 'k'}, {'first': 'Hernan', 'last': 'w'}, {'first': 'C', 'last': 'l'},{'first': 'Z', 'last': 'k'}]

print(sorted(items, key=itemgetter('last')))
print(sorted(items, key=lambda x: x['last']))  # alternative

print(sorted(items, key=itemgetter('last', 'first')))
print(sorted(items, key=lambda x: (x['last'], x['first']))) #alternative using array syntax

#other funcs like min, max