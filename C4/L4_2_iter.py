__author__ = 'Hernan Y.Ke'
#implement __iter__

class No:
    def __init__(self, value):
        self._value=value
        self.container =[]

    def add_child(self,node):
        self.container.append(node)

    def __repr__(self):
        return '{!r}'.format(self._value)

    def __iter__(self):
        return iter(self.container)


if __name__=='__main__':
    root = No(1)
    child1 = No(10)
    child2 = No(20)
    root.add_child(child1)
    root.add_child(child2)
    for c in root:
        print(c)