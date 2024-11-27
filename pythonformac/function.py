#!/usr/bin/python3
#Filename:function.py
#在函数中变量是局部的
def f1():
    i=5
    return i
i=4
print(i)
print(f1())

#可用global变为全局(函数内没有同名变量)
def f2():
    global x
    print(x)
    x=4
    print(x)
x=5
f2()
print(x)

#设置默认值，在末尾
def f3(a,b=2):
    print(a*b)
f3(2)
f3(2,5)

#关键参数
def f4(i1,i2=50,i3=100):
    print('''i1=%d,i2=%d,i3=%d'''%(i1,i2,i3))
f4(10)
f4(i2=80,i1=70)

#没有指定return时
def f5():
    pass
f5()

def f6():
    return
f6()

#docstrings文档字符串
def max(a,b):
    '找出两数的最大值'
    if a>b:
        print(a)
    elif a<b:
        print(b)
    else:
        print('a=b')
max(1,2)
#输出函数字符串
print(max.__doc__)
