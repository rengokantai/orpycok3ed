__author__ = 'Hernan Y.Ke'

# you want to add extra processing to getting and setting methods
class A:
    def __init__(self,prop):
        self.prop=prop

    @property
    def prop(self):
        return self._prop

    @prop.setter
    def prop(self,prop):
        if not isinstance(prop,str):
            raise TypeError('must be string')
        self._prop=prop

    @prop.deleter
    def prop(self):
        raise AttributeError('cannot delete')


p=A("100")
p.prop="200"
#p.prop=200  #error,should be str
print(p._prop)
