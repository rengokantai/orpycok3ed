__author__ = 'Hernan Y.Ke'
from collections import namedtuple

# memorize this syntax
Me = namedtuple('Me',['first','last'])
me = Me(1,2)
print(me.first,me.last)

she=[Me(3,4),Me(5,6)]


#me = Me(first=1,last=2)    # illegal!

me = me._replace(first=3)
print(me.first)

# get namedtuple
def get_num(tuplearr):
    res=0
    for param in tuplearr:
        s = Me(*param)  # iterate a array with namedtuple instance. param->All params of a instance
        res+=s.first+s.last
    return res

print(get_num(she))


#replace all params
def replace_params(tupleparams):
    return me._replace(**tupleparams)     # two stars.  kwargs

newparams={'first':7,'last':8}
print(replace_params(newparams))