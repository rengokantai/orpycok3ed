__author__ = 'Hernan Y.Ke'

arr=['a','b','c']
for index,item in enumerate(arr,1):  #index start from 1
    print(index, item)



# for tuple array:

tuplearr =[('a','b'),('c','d'),('e','f')]

for index,(x,y)in enumerate(tuplearr,1):
    print(index, x, y)