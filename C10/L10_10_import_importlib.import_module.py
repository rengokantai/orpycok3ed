__author__ = 'Hernan Y.Ke'
import importlib

math = importlib.import_module('math')
print(math.sin(30))
req = importlib.import_module('urllib.request')
url = req.urlopen('http://google.com')