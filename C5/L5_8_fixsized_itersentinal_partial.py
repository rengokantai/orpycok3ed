__author__ = 'Hernan Y.Ke'
from functools import partial

REC = 32
with open('data','rb') as f:
    rec = iter(partial(f.read,REC),b'')     #remember the syntax: iter(partial(filename.read, chunksize)