__author__ = 'Hernan Y.Ke'

#class with one method
class ClassName:
    def __init__(self,container):
        self.container = container
    def open(self, **kwargs):
        return self.container(kwargs)

#single function
def classname(container):
    def open(**kwargs):
        return container(kwargs)

