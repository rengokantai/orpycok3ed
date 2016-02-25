__author__ = 'Hernan Y.Ke'
from operator import attrgetter

class Me:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '{}'.format(self.id)

arr=[Me(1),Me(3),Me(2)]

print(sorted(arr,key=attrgetter('id')))#slightly faster.
print(sorted(arr,key=lambda x:x.id))    #Dot notation.