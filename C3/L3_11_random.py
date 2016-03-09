__author__ = 'Hernan Y.Ke'
import random

arr=[1,2,3,4]
print(random.choice(arr))
print(random.sample(arr,3))
print(random.shuffle(arr))


# produce random int
print(random.randint(0,10))  #0<=x<=10

#0 to 1
print(random.random())

#bits
print(random.getrandbits(100))

#others
random.seed()