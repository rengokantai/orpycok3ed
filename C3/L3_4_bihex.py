__author__ = 'Hernan Y.Ke'
import os

x = 123

# with prefix
print(oct(x), bin(x), hex(x))

# no prefix
print(format(x, 'x'))

#produce unisgned num

y = -123
print(format(2 ** 32 + y, 'b'))

#convert base

print(int('1111011', 2))  #first param must be str type

#change previlege:
os.chmod('file', 0o755)  #correct.
#os.chmod('file',0755)  #incorrect.