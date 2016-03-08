__author__ = 'Hernan Y.Ke'
from fnmatch import fnmatch,fnmatchcase

print(fnmatch('a.txt','*.txt'))   #syntax: actualword, re

#in python, * = any number of char

#However, windows regex match is non case-sensitive (on mac is case-sensitive)

print(fnmatch('a.txt','*.TXT'))

#using fnmatchcase
print(fnmatchcase('a.txt','*.TXT'))