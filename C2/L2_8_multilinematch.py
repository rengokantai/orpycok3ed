__author__ = 'Hernan Y.Ke'

import re

commentre=re.compile(r'/\*(.*?)\*/')

single = '/* comment */'
multi = '''/*
comment
*/'''
print(commentre.findall(single))
print(commentre.findall(multi))

# using noncapture group  ?:

multicommentre=re.compile(r'/\*((?:.|\n)*?)\*/')    # .=char \n=newline
print(multicommentre.findall(single))
print(multicommentre.findall(multi))