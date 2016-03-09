__author__ = 'Hernan Y.Ke'
from datetime import datetime

text='2016-03-05'

day1 = datetime.strptime(text,'%Y-%m-%d')

day2 = datetime.today()

inter = day2-day1

print(inter)

fulldate = datetime.strftime(day2,'%A %B %d %Y')   # memorize %A %B %d %Y

print(fulldate)