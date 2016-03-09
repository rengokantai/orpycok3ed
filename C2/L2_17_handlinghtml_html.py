__author__ = 'Hernan Y.Ke'
import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape
htmlstr='writing "<b>strong</b>"'

print(html.escape(htmlstr))
print(html.escape(htmlstr,quote=False))
# html.parser.HTMLParser.unescape will be deprecated

# unescape xml
print(unescape(html.escape(htmlstr)))

#unescape html
print(html.unescape(html.escape(htmlstr)))