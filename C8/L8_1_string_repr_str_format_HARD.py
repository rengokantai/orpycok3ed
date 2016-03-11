__author__ = 'Hernan Y.Ke'
class Pt:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return '({0.x!s},{0.y!s})str'.format(self)
    def __repr__(self):
        return '({0.x!r},{0.y!r})repr'.format(self)
p=Pt(1,2)
p
print(p)