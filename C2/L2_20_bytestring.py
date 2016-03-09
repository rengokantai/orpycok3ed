__author__ = 'Hernan Y.Ke'
import re
str1 = b'hen,cat:dog'

print(str1.replace(b'cat',b'dog'))

byte1 = bytearray(str1)
print(byte1.replace(b'cat',b'dog'))

print(re.split(b'[:,]',str1))

#return byte
print(str1[0])

#DECODE TO STRING
print(str1.decode('ascii'))

#align

print('{:^10.2f}'.format(100.1).encode('ascii'))