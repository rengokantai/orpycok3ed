__author__ = 'Hernan Y.Ke'
from decimal import Decimal,localcontext,getcontext
import math

a = Decimal('4.2')
b = Decimal('1.1')
#check from python doc
print(Decimal(3.553).quantize(Decimal('.01')))
print(a+b)

getcontext().prec=5
print(a/b)

arr =[1.2e+18,1,-1.2e+18]
print(sum(arr)) #not accurate
print(math.fsum(arr))


