__author__ = 'Hernan Y.Ke'
import re
from collections import namedtuple

NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z0-9]*)'
NUM = r'(?P<NUM>\d+)'
EQ=r'(?P<EQ>=)'
WS=r'(?P<WS>\s+)'


masre = re.compile('|'.join([NAME,NUM,EQ,WS]))

scanner = masre.scanner('ke = 10')
_ = scanner.match()
print(_.lastgroup,_.group())
_ = scanner.match()
print(_.lastgroup,_.group())
_ = scanner.match()
print(_.lastgroup,_.group())
_ = scanner.match()
print(_.lastgroup,_.group())
_ = scanner.match()
print(_.lastgroup,_.group())


print('---------')

Token = namedtuple('Token',['type','value'])

def gene_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup,m.group())

for k in gene_tokens(masre, 'ke=10'):
    print(k)