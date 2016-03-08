__author__ = 'Hernan Y.Ke'

import re

sentence = 'a b; c,   d'
print(re.split(r'[;,\s]\s*',sentence))