__author__ = 'Hernan Y.Ke'
import pkgutil
class C:
    def pr(self):
        print('C')


data = pkgutil.get_data('__package__', 'a.py')
print(data)
