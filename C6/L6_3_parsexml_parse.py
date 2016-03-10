__author__ = 'Hernan Y.Ke'
from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen("http://planet.python.org/rss20.xml")
d = parse(u)

for item in d.iterfind('channel/item'):  #return non-child node
    title = item.findtext('title')
    print(title)
    print(title.tag)
    print(title.text)