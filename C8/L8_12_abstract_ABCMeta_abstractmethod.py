__author__ = 'Hernan Y.Ke'
from abc import ABCMeta,abstractmethod
from decimal import Decimal
import numbers,io,os

class IS(metaclass=ABCMeta):
    @abstractmethod
    def read(self,mb=-1):
        pass
    @abstractmethod
    def write(self,data):
        pass

IS.register(io.IOBase)
f = open(os.path.abspath(os.getcwd())+'\\L8_9_.py')
print(isinstance(f,IS))


x = Decimal('2.3')
print(isinstance(x,numbers.Real))

