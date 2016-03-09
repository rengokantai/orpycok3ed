__author__ = 'Hernan Y.Ke'
from fractions import Fraction

a=Fraction(3,2)
b=Fraction(7,4)

c=a*b
print(c,c.numerator,c.denominator,float(c),c.limit_denominator(4))

x=4.33
print(Fraction(*x.as_integer_ratio()).limit_denominator(4)) #regard this x as tuple  max demoniator = limit - 1