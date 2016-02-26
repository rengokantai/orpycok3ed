__author__ = 'Hernan Y.Ke'

import os

files = os.listdir(os.getcwd())

if any(name.endswith('py') for name in files):
    print('works')
else:
    print()



#performance test

testdict = [{
                'A': 100,
                'B': 10
            }, {
                'A': 200,
                'B': 10
            }, {
                'A': 100,
                'B': 10
            }]

print(min(testdict,key=lambda x:x['A']))
print(min(x['A']for x in testdict))  # better
