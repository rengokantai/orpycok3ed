__author__ = 'Hernan Y.Ke'
names=['hernan Ke','z Wang','lex A']

print(sorted(names,key=lambda x:x.split(" ")[-1].lower()))