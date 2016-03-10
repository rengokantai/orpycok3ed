__author__ = 'Hernan Y.Ke'

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

    def dfs(self):
        return DFS(self)

class DFS(object):
    def __init__(self, start_node):
        self._node = start_node
        self._childreniter= None
        self._childiter=None

    def __iter__(self):
        return self

    def __next__(self):
        if self._childreniter is None:
            self._childreniter = iter(self._node)
            return self._node

        elif self._childiter:
            try:
                nextchild = next(self._childiter)
                return nextchild
            except StopIteration:
                self._childiter=None
                return next(self)
        else:
            self._childiter = next(self._childreniter).dfs()
            return next(self)

