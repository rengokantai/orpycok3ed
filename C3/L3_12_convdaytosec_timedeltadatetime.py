__author__ = 'Hernan Y.Ke'
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

#doing arithmetic
a= timedelta(days=2,hours=3)  #using plural
b = timedelta(hours=1)

c=a+b
print(c.days,c.seconds,c.total_seconds(),c.seconds) #total_seconds: with day  seconds: within day


n = datetime.today()
print(n+timedelta(days=4))
o = datetime(2009,1,1)
inter=n-o
print(inter)
print(inter.days)


#print all units
print(relativedelta(n,o))       #main syntax between timedelta and relativedelta
print(n+relativedelta(months=+3))
