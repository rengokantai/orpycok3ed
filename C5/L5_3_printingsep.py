__author__ = 'Hernan Y.Ke'
print(1,2,3,sep=',',end='!!')

for x in range(0,2):
    print(x,end='\n!')

print('--')
arr=[1,2,3]

print(','.join(str(x) for x in arr))
#same as
print(*arr,sep=',')