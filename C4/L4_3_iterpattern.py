__author__ = 'Hernan Y.Ke'

def iterpat(start,stop,step):
    while start<stop:
        yield start
        start+=step

for x in iterpat(1,3,0.5):
    print(x)


#OR

inst = iterpat(1,3,0.5)

print(next(inst))
print(next(inst))
print(next(inst))

