__author__ = 'Hernan Y.Ke'

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


class B(A):
    @property
    def prop(self):
        print("name")
        return super().prop

    @prop.setter
    def prop(self,prop):
        print("super")
        super(B,B).prop.__set__(self,prop)

    @prop.deleter
    def prop(self):
        print('delete')
        super(B,B).prop.__delete__(self)
    @prop.getter
    def prop(self):
        print('get')
        return super().prop


p=B("100")
p.prop="200"
#p.prop=200  #error,should be str
print(p.prop)
