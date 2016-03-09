__author__ = 'Hernan Y.Ke'

deci = 12345.6789
print(format(deci,'^10.1f'))
print(format(deci,'e'))
print(format(deci,'0.2E'))
print(format(deci,','))
print(format(deci,'0,.1f'))

print(format(-deci,'0,.1f'))
print('{:0,.2f}'.format(-deci))

#review old style (can not use commas in old style)
print('%10.1f' % deci)
#print(deci.format('^10.1f')) incorrect.   Please Review L2_15  AttributeError: 'float' object has no attribute 'format'

print('-------')
# translate: note: key must be integer. using ord to translate. Review L2_12
#swap_sep = {'.':',',',':'.'} error@
swap_sep = {ord('.'):',',ord(','):'.'}
print(format(format(deci,',').translate(swap_sep)))