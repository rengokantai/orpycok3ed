__author__ = 'Hernan Y.Ke'

from operator import itemgetter
from itertools import groupby

items = [{'first': 'Hernan', 'last': 'k'}, {'first': 'Hernan', 'last': 'w'}, {'first': 'C', 'last': 'l'},{'first': 'Z', 'last': 'k'}]

items.sort(key=itemgetter('last')) # already sorted. no not to assign to a new var.

for last,item in groupby(items, key=itemgetter('last')):
    print(last)
    for i in item:
        print(i)