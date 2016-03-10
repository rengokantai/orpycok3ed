__author__ = 'Hernan Y.Ke'
import heapq

arr1= [1,2,5,19]
arr2= [4,12,15,25]

for i in heapq.merge(arr1,arr2):
    print(i)