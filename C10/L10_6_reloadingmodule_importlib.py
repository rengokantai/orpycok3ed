__author__ = 'Hernan Y.Ke'
import importlib
from C10.mypkg import a
from C10.mypkg import b

importlib.reload(a)


# in the book, `imp` module is deprecated