__author__ = 'Hernan Y.Ke'

arr = [1,2,3,4,5,6,7]

print(arr[1:5:2])


#slice naming. Avoid hard-coded slice
slicename = slice(1, 5,2)     #Note the syntax. Not square bracket, not colon

print(arr[slicename])

sen="customsentence"

print(slicename.indices(len(sen)))

for i in range(*slicename.indices(len(sen))):
    print(sen[i])
