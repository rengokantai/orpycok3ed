__author__ = 'Hernan Y.Ke'

x =1
a = lambda y:x+y    #run time
c= lambda y, x=x:x+y #bind at def time
x=2
b=lambda y:x+y  #run time
d= lambda y, x=x:x+y    #def time
print(a(10))
print(b(10))
print(c(10))
print(d(10))

#problem is the value of x used in the lambda expression is free var get bound at runtime,not def time