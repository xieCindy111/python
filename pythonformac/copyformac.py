#!/usr/bin/python3
#Filename:copyformac.py
a = [1,2,8,4,5]
#用[:]可以复制a数列的所有值
b = a[:]
print(b)
c=a[0:3:2]
#输出的c即[1,8]
print(c)
#深度复制
import copy
d=copy.deepcopy(a)
a=[i*2 for i in a]
print(a)
print(d)


