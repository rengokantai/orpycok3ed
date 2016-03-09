__author__ = 'Hernan Y.Ke'
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

n =datetime.now()

print(n+relativedelta(weekday=FR))   #next friday
print(n+relativedelta(weekday=FR(-1)))  #last friday