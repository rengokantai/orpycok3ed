__author__ = 'Hernan Y.Ke'
import os.path
import os
def read_in_buf(file):
    buf =bytearray(os.path.getsize(file))
    with open(file,'rb')as f:
        f.readinto(buf)         #read bytearray into buffer
    return buf

with open('text1.txt','wb')as f:
    f.write(b'hello')

buf = read_in_buf(os.getcwd()+'\\text1.txt')
print(buf)
buf[0:3]=b''        #change buffer content
print(buf)

with open(os.getcwd()+'\\text2.txt','wb')as f:
    f.write(buf)        #write buffer type