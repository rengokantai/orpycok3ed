__author__ = 'Hernan Y.Ke'
a = {'a': 1, 'c': 3, 'e': 5}
b = {'b': 1, 'd': 3, 'e': 5}

print(a.keys() - b.keys())
print(a.keys() & b.keys())
print(a.items() & b.items())

c = {key:a[key] for key in a.keys()-{'a'}}  #bracket notation
print(c)