__author__ = 'Hernan Y.Ke'
class Base:
    def __init__(self):
        print("base")

class A(Base):
    def __init__(self):
        super().__init__()
        print("A.init")

class B(Base):
    def __init__(self):
        super().__init__()
        print("B.init")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C.init")

c = C()
print(c)
print(C.__mro__)
print(C.mro())

