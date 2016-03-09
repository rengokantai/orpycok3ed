__author__ = 'Hernan Y.Ke'

import re
print('-=-string=='.strip('-='))

spacestring='  string  '
# cut all spaces

print(re.sub('\s+','',spacestring))