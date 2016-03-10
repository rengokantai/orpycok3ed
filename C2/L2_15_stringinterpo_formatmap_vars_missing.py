__author__ = 'Hernan Y.Ke'
import string,sys
temp = 'Here is {var}'

print(temp.format(var='cat'))  # review syntax of str.format

var='cat'



print(temp.format_map(vars()))
str2 = string.Template('$var')
print(str2.substitute(vars()))

# print('Here is %(var)' % vars())   STILL NOT WORKING.

#using instance:

class Info:
    def __init__(self,name,n):
        self.name=name
        self.n=n

a =Info("ke",10)
str3 = '{name}{n}'
print(str3.format_map(vars(a)))

#handling missing value, create a placeholder

name='ke'

class safesub(dict):        #must use `dict` keyword here
    def __missing__(self,key):
        return '{'+key+'}'

print(str3.format_map(safesub(vars())))


#define a utility function:
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

#Test

n=10

print(sub('{name}'))
print(sub('{n}'))