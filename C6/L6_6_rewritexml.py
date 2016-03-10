__author__ = 'Hernan Y.Ke'
from xml.etree.ElementTree import parse,Element

d = parse('p.xml')
root = d.getroot()
print(root)

root.remove(root.find('sri'))
root.remove(root.find('cr'))
root.getchildren().index(root.find('nm'))

newelem = Element('ke')
newelem.text = 'ke'
root.insert(2,newelem)  #insert after index 2 based on root parent.

d.write('p2.xml','utf-8',xml_declaration=True)