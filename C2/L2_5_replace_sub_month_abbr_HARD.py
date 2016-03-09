__author__ = 'Hernan Y.Ke'
import re
from calendar import month_abbr

sen = "cat and dog, cat"

print(sen.replace('cat','cap',1))


datestring = "01/02/2010"


"""
re.sub(pattern,newpattern,word)
OR
re.compile(oldpattern)
then .sub(newpattern,word)
"""
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',datestring))
print(re.subn(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',datestring).index(1))    #count matching time


# sub using callback

datepart = re.compile(r'(\d+)/(\d+)/(\d+)')

def cgdate(match):
    mname=month_abbr[int(match.group(1))]
    return'{} {} {}'.format(match.group(2),mname, match.group(3))

print(datepart.sub(cgdate,datestring))








