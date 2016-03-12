__author__ = 'Hernan Y.Ke'
# from .a import A
# from .b import B

#lazy
def A():
    from .a import A
    return A()

def B():
    from .b import B
    return B()