__author__ = 'Hernan Y.Ke'
from datetime import timezone,datetime,timedelta
from  pytz import timezone


#other region->local time
date1 = datetime.now()
zonenow = timezone('US/Central')

loc_d = zonenow.localize(date1)    #timezone.localize(time)



print(loc_d)

#local time->other region time

othertime= loc_d.astimezone(timezone('Asia/Kolkata'))           #time.astimezone(otherzone)
print(othertime)



#for daylight saving

latertime = zonenow.normalize(loc_d+timedelta(minutes=30))
print(latertime)