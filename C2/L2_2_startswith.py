__author__ = 'Hernan Y.Ke'
import os
choices=['a','b']
print('abc'.startswith(tuple(choices))) # startswith first arg must be str or a tuple of str, not list


#matching test

if any(name.endswith('py') for name in os.listdir(os.getcwd())):
    print('works')

