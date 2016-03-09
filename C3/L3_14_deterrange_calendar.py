__author__ = 'Hernan Y.Ke'
import calendar
from datetime import datetime,date,timedelta


#dummy way
def listrange(start, stop, interval):
    while start<stop:
        yield start
        start+=interval

for d in listrange(datetime(2001,1,1),datetime(2001,1,5),timedelta(hours=12)):
    print(d)



# advanced

def get_month_range(start_date=None):
    if start_date is None:
        start_date=date.today().replace(day=1)   #syntax1   date.doday replace
    _,dateinmonth = calendar.monthrange(start_date.year,start_date.month) #syntax2,      monthrange(year,month)  return two prams.
    end_date=start_date+timedelta(days=dateinmonth)
    return  (start_date,end_date)

d = timedelta(days=1)

fd,ld = get_month_range()
while fd<ld:
    print(fd)
    fd+=d
