__author__ = 'Hernan Y.Ke'
txt="word"
#align left
print(txt.ljust(6))
print(txt.format('<6'))        #syntax1
print('{:<6}'.format(txt))
print('%-6s'% txt)

#align right
print(txt.rjust(6))
print(format(txt,'>6'))         #alternative syntax
print('{:>6}'.format(txt))
print('%6s'% txt)
#align center
print(txt.center(6))
print(format(txt,'^6'))
print('{:^6}'.format(txt))
#fill char
print(txt.center(6,'*'))
print(format(txt,'*^6'))



