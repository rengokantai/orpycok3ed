__author__ = 'Hernan Y.Ke'
from array import array
with open('','rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('','wb') as f:
    f.write(b'')
    text='abc'
    f.write(text.encode('utf-8'))

shortarr = array('i',[1,2,3])
with open('text1.txt','wb') as f:
    f.write(shortarr)

arr = array('i',[0,0,0,0,0,0,0,0])
with open('text1.txt','rb') as f:
    f.readinto(arr)

print(arr)