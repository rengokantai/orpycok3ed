__author__ = 'Hernan Y.Ke'
import gzip,bz2
with gzip.open('a.gz','rt') as f:
    test =f.read()

with bz2.open('a.bz2','rt') as f:
    test =f.read()

with gzip.open('a.bz2','wt',compresslevel=5) as f:  #default=9, highest,level of compression
    f.write()

#on top of binary mode
f = open('x.gz','rb')
with gzip.open(f,'rt') as g:
    text = g.read()

