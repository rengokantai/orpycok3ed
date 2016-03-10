__author__ = 'Hernan Y.Ke'
from xml.etree.ElementTree import iterparse

def parse_xml(filename,path):
    path_part =path.split(',')
    doc = iterparse(filename,('start','end'))

    next(doc)   #skip root

    tagarr=[]
    elemarr=[]

    for event,elem in doc:
        if event== 'start':
            tagarr.append(elem.tag)
            elemarr.append(elem)
        elif event=='end':
            if tagarr == path_part:
                pass
            #not completed.



