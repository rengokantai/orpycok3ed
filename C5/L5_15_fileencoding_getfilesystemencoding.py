__author__ = 'Hernan Y.Ke'
# handling exception
import sys
import os
#version 1
def badfile(filename):
    return repr(filename)[1:-1]

#version 2
def badfilename(filename):
    temp = filename.encode(sys.getfilesystemencoding(),errors='surrogateescape')
    return temp.decode('latin-1')

#read
for file in os.listdir(os.path.abspath(os.getcwd())):
    try:
        print(file)
    except UnicodeEncodeError:
        print(badfilename(file))