__author__ = 'Hernan Y.Ke'
import html

def makeelem(name,**kwargs):
    keyval =[ '%s="%s"' % item for item in kwargs.items()]
    #keyval=['{}'.format(kwargs.items())] failed using python 3.4
    attrstr = ' '.join(keyval)
    elems = '<{name} {kwargs}></{name}>'.format(name=name,kwargs=attrstr)
    return elems

print(makeelem('li',size=1,max=100))