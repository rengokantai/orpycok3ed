__author__ = 'Hernan Y.Ke'
import re

"""
Note r'\d' == '\\d'
"""
#stack.find(needle)
print("stack".find('s'))


#re.match(regex,word)
print(re.match(r'\d+','100'))


#re.compile(regex).match(word)
print(re.compile(r'\d+').match('100'))

#re.compile(regex).findall(word)
print(re.compile(r'\d').findall('100'))

#grouping.
print(re.compile(r'(\d)(\d)(\d)').match('100').group(0))
print(re.compile(r'(\d)(\d)(\d)').match('100').group(1))
print(re.compile(r'(\d)(\d)(\d)').match('100').groups())


print("-------")
#match iteratively
for i in re.compile(r'(\d)(\d)(\d)').finditer('100 100'):
    print(i.groups())