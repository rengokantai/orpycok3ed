__author__ = 'Hernan Y.Ke'
import base64

st =b'ke'
a = base64.b64encode(st)
print(a)
asc = a.decode('ascii')
print(asc)
st = base64.b64decode(a)
print(st)