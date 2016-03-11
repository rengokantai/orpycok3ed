__author__ = 'Hernan Y.Ke'

from datetime import date

d =date(2016,1,1)
print(format(d,'%A%B%d%Y'))
#alternative
print('{:%A%B%d%Y}'.format(d))

print('---')
_fom={
    'ymd':'{d.year}-{d.mon}-{d.day}',
    'mdy':'{d.mon}/{d.day}/{d.year}'
}

class Date:
    def __init__(self,year,mon,day):
        self.year = year
        self.mon=mon
        self.day=day
    def __format__(self, format_spec):
        if format_spec=='':
            format_spec='ymd'
        fmt = _fom[format_spec]
        return fmt.format(d=self)

dt= Date(2016,1,1)
#print(dt.format())  # object has no attribute 'format'(incorrect)

print(format(dt,'mdy'))
print('{:mdy}'.format(dt))