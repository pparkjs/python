# 로또
from random import random

arr = []

for i in range(1, 46):
    arr.append(i)

for i in range(46):
    rnd = int(random() * 45)
    a = arr[rnd]
    b = arr[0]
    arr[0]=a
    arr[rnd]=b

print(arr[0:6])