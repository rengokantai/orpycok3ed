__author__ = 'Hernan Y.Ke'
from xml.etree.ElementTree import Element, tostring
def dict_to_xml(tag,d):
    elem = Element(tag)
    for key,val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem
    # Element->parent elem,   child-> child elem child.text: chilren's text

dic = {'name':'k','age':10}
inst = dict_to_xml('topelem',dic)
print(tostring(inst))

inst.set('_id','k')
print(tostring(inst))

# to be continued