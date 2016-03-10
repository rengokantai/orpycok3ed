__author__ = 'Hernan Y.Ke'
#naive

CHUNK =1000

def reader_naive(da):
    while True:
        data = da.recv(CHUNK)
        if data == b'':
            break

#revamp:
def reader(da):
    for ck in iter(lambda da:da.recv(CHUNK),b''):     # second param is stop flag!
        pass

#test

def adda(a,b):
    return a+b

x=0

for x in iter(lambda :adda(x,3),12):    # no lambda x:....
    print(x)
#second param can not use a function. What if I want to stop when value is higher than 12?


def getx(x):
    return x==12