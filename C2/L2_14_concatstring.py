__author__ = 'Hernan Y.Ke'

#join string more efficient
a='a'
b='b'
print(a+':'+b)
print(':'.join([a,b]))
print(a,b,sep=':') #better


#fetch from yield
def fetchab():
    yield 'a'
    yield 'b'

print(':'.join(fetchab()))

