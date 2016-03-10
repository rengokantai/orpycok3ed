__author__ = 'Hernan Y.Ke'
import os
if not os.path.exists('text1.txt'):
    with open('','rb') as f:
        data = f.read(16)
        text = data.decode('utf-8')