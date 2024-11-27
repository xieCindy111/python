import random
import time
#询问是否开始游戏
p=input('start or not:')
while p=='start':
#初始化界面
    a=5
    b=5
    l=[]
    for i in range(a):
        l.append([])
        for j in range(b):
            l[i].append('*')
    def start():
        for i in range(a):
                for j in range(b):
                    if j!=4:
                        print(l[i][j],end=' ')
                    else:
                        print(l[i][j],end='\n')
    start()
    def find(l):
        n0=0
        for i in range(5):
            for j in range(5):
                if l[i][j]=='*':
                    n0+=1
        return n0
#定义地雷数量
    num=random.randint(1,3)
    print('There are %d bomb here'% num)
#定义地雷位置
    d=[]
    for i in range(num):
        x=random.randint(1,5)
        y=random.randint(1,5)
        d.append([x,y])
    def f(xt,yt):
        if [xt,yt] in d:
            return '#'
        else:
            m=0
            for i in range(xt-1,xt+2):
                for j in range(yt-1,yt+2):
                    if [i,j] in d:
                        m+=1
            return m
    you='start'
    n=0
    n0=0
    while you=='start':
#用户点击位置
        xt=int(input('你想点击的区域（行）:'))
        yt=int(input('你想点击的区域（列）:'))
        if xt>5 or yt>5:
            print('you hit a wrong area')
            xt=int(input('你想点击的区域（行）:'))
            yt=int(input('你想点击的区域（列）:'))
        l[xt-1][yt-1]=f(xt,yt)
        if l[xt-1][yt-1]=='#':
            start()
            print('you hit a bomb')
            you='end'
        else:
            start()
            n0=find(l)
            if n0==num:
                you='win'
                print('you win')
#扫雷结束后暂停3秒询问是否继续下一轮
    time.sleep(3)
    p=input('start or not:')

   
